# Djangoのインストール方法
`pip`を用いたインストール
```
pip install django
```

# Djangoを使ってみる

## Project を作成する
適当なディレクトリに`django`用のディレクトリを作成する.
```
$ mkdir django
$ cd django
$ django-admin startproject start
$ cd first
$ ls
manage.py	start
```
開発用サーバーを開いてみる.
```
$ python3 manage.py runserver  
(省略)
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
 http://127.0.0.1:8000/ をブラウザで開く.
 
## Application を作成する
```
 $ python3 manage.py startapp myapp
```
