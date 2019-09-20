from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, create_access_token,
    get_jwt_identity, get_jti, get_raw_jwt, get_current_user
)
from util.db import DB
import bcrypt
import traceback

app = Blueprint('user', __name__, url_prefix='/api/v1')

@app.route('/sign_in', methods=['post'])
#@fresh_jwt_required
def sign_in():
    try:
        name = request.json.get("name")
        password = request.json.get("password")
        sql = "SELECT id, name, password FROM users WHERE BINARY name=%s"
        db = DB
        user = db.execute(sql, [ name ])
        if not (user and bcrypt.checkpw(password.encode(), user['password'].encode())):
             return jsonify( {"message": "ユーザー名又はパスワードが違います。"} ), 401
    except Exception as e:
        traceback.print_exc()
        return jsonify( {"message": "An error occurred"} ), 500

    access_token = create_access_token(identity=user["id"], fresh=True)
    sql = "UPDATE users SET jti=%s WHERE name=%s"
    DB.update(sql, [ get_jti(access_token), 'python' ])
    sql = "SELECT name, jti FROM users"
    user = DB.execute_list(sql)
    return jsonify(access_token=access_token), 200

@app.route("/protected", methods=["GET"])
@fresh_jwt_required
def protected():
    user = auth_jti(get_jwt_identity(), get_raw_jwt()["jti"])
    if not user:
        return jsonify( {"message": "Bad access token"} ), 401
    return jsonify( user ), 200

@app.route("/sign_out", methods=["GET"])
@fresh_jwt_required
def sign_out():
    print(get_jwt_identity())
    sql = "UPDATE users SET jti=null WHERE id=%s"
    DB.update(sql, [ get_jwt_identity() ])

    return '', 204

def auth_jti(id, token_jti):
    sql = "SELECT id, name, jti FROM users WHERE id=%s"
    user = DB.execute(sql, [ id ])
    if token_jti == user["jti"]:
        return user
    return False
