from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, create_access_token,
    get_jwt_identity, get_jti, get_raw_jwt, get_current_user
)
from util.db import DB
import bcrypt
import traceback
import re

app = Blueprint('user', __name__, url_prefix='/api/v1')

@app.route('/sign_in', methods=['post'])
#@fresh_jwt_required
def sign_in():
    try:
        db = DB()
        db.connect()
        name = request.json.get("name")
        password = request.json.get("password")
        sql = "SELECT id, name, password FROM users WHERE BINARY name=%s"
        user = db.execute(sql, [ name ])
        if not (user and bcrypt.checkpw(password.encode(), user['password'].encode())):
             return jsonify( {"message": "ユーザー名又はパスワードが違います。"} ), 401
    except Exception as e:
        traceback.print_exc()
        return jsonify( {"message": "ログイン処理でエラーが発生しました。"} ), 500

    access_token = create_access_token(identity=user["id"], fresh=True)
    sql = "UPDATE users SET jti=%s WHERE name=%s"
    db.update(sql, [ get_jti(access_token), name ])
    db.commit()
    return jsonify(access_token=access_token), 200

@app.route("/protected", methods=["GET"])
@fresh_jwt_required
def protected():
    user = auth_jti(get_jwt_identity(), get_raw_jwt()["jti"])
    if not user:
        return jsonify( {"message": "アクセストークンが間違っています。"} ), 401
    return jsonify( user ), 200

@app.route("/sign_out", methods=["GET"])
@fresh_jwt_required
def sign_out():
    db = DB()
    db.connect()
    sql = "UPDATE users SET jti=null WHERE id=%s"
    db.update(sql, [ get_jwt_identity() ])
    db.commmit()
    return '', 204

@app.route("/sign_up", methods=["POST"])
def signup():
    db = DB()
    db.connect()
    data = request.get_json()
    name = data["name"]
    password = data["password"]
    password_conf = data["password_conf"]

    if name and name.encode().isalnum() and password != password_conf:
        return jsonify( {"message": "ユーザー名又はパスワードが正しく入力されていません。"} ), 400

    sql = "SELECT * FROM users WHERE name=%s"
    if db.execute(sql, [ name ]):
        return jsonify( {"message": "このユーザー名は既に使われています。"} ), 400
    else:
        salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
        hashed_pass = bcrypt.hashpw(password.encode(), salt).decode()
        sql = "INSERT INTO users (name, password) VALUE (%s, %s)"
        db.update(sql, [ name, hashed_pass ])
        db.commit()
        return jsonify( {"message": "Completed"} ), 200

def auth_jti(id, token_jti):
    db = DB()
    db.connect()
    sql = "SELECT id, name, jti FROM users WHERE id=%s"
    user = db.execute(sql, [ id ])
    if token_jti == user["jti"]:
        return user
    return False

alnum_Reg = re.compile(r'^[a-zA-Z0-9_]+$')
def isalnum_(s):
    return alnum_Reg.match(s) is not None
