# venvとは
venv(virtual environment)とは, 仮想環境のこと.  
venvを使うことで, 作りたいもの専用の環境を作ることができる.

## venvを使ってみる

```
$ python3 -m venv myvenv
```
`myvenv`というディレクトリが作成される.
```
$ cd myvenv
$ source bin/activate
```
とすると, (myvenv)が有効になる.  
(myvenv)を終了する時は, 
```
$ deactivate
```

## 他人と共同開発する場合

開発環境のエクスポート
```
$ pip freeze > requirements.txt
```
開発環境のインポート
```
$ pip install -r requirements.txt
```
