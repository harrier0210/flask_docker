# 環境構築手順

## git clone

* git clone

## docker install

* 下記からdocker for windows をインインストール
 * ※docker hubのアカウント登録する必要あり
 * https://docs.docker.com/docker-for-windows/install/

 * 参考サイト
 * https://ops.jig-saw.com/techblog/docker-for-windows-install/


## install後の設定

* 画面右下のクジラのアイコンクリック
* docker switch to linux containersをクリック
* 再度クジラのアイコンクリック
* settings
* shared drives
* 「C」を選択してapply

## コンテナ起動

* docker-compose up -d --build
* localhost:5000 にアクセス
* docker-compose stop でコンテナ停止
* docker exec -it flask sh でコンテナ内に入れる


* 参考サイト
* https://qiita.com/ksh-fthr/items/6b1242c010fac7395a45
