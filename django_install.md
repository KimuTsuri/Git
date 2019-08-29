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
settings.py を編集
```
(省略)  
INSTALLED_APPS = [
    'myapp.app.MyappConfig' #追加
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]  
(省略)  
```
urls.py を編集
```
from django.contrib import admin
from django.urls import path, include #includeを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'), #追加
]
```
myappディレクトリ内に`urls.py`を作成し
```
from django.urls import path
from .import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
]
```
とする.  
views.pyを編集する.
```
from django.shortcuts import render
from django.http import HttpResponse #追加
# Create your views here.

def index(request):
    return HttpResponse("Hello, World") #追加
```
ここまで出来たら実行してみる.
```
$ python3 manage.py runserver
```
