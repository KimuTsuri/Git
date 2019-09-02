# 初めてのHTML

```
<!doctype html>
<html>
  <head>
    <title>初めてのHTML</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Hello, World</h1>
  </body>
</html>
```

* `<!doctype html>` : html形式を使うという宣言.
* `<html>` : htmlの内容を中に書く.
* `<head>` : タイトルや, 文字コードの設定, ページの情報などを書く.
* `<body>` : 実際に画面に表示する内容を書いていく.

# 初めてのCSS

## class

classの書き方
```
.midasi{
 color:blue;
 background-color:black;
}
```
class の適用方法
```
<h1 class="midasi"> </h1>
```

## id

idの書き方
```
#midasi{
 color:blue;
 background-color:black;
}
```
注意! 同じid名を2度使うことは出来ない.  
id の適用方法
```
<h1 id="midasi"> </h1>
```

## <h1>を直接変更する方法
```
h1{
 font-size:50px;
}
```

## CSSをファイルに書く
css を定義したファイルを作成する."hoge.css"を用意した場合, <head>内に
```
<link rel="stylesheet" href="hoge.css">
```
を追加することでCSSの内容を適用させることができる.

