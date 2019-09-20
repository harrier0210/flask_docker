# ベースイメージとして python v3.7 を使用する
FROM python:3.7.2-alpine

# 以降の RUN, CMD コマンドで使われる作業ディレクトリを指定する
WORKDIR /app

# カレントディレクトリにある資産をコンテナ上の ｢/app｣ ディレクトリにコピーする
ADD . /app

# ｢ requirements.txt ｣にリストされたパッケージをインストールする
RUN apk --no-cache add alpine-sdk libffi-dev python-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Docker イメージ中の環境変数を指定する
ENV NAME World
