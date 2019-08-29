# 数値

## 基本的な演算

```
>>> 1 + 1
2
>>> 2 - 1
1
>>> 1 * 2
2
>>> 10 ** 2
100
>>> 10 ** 0
1
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

## 変数とは

変数とは、メモリ作成した object にアクセスする名前.

```
>>> a = 1 + 1
>>> b = 10 + 10
>>> c = a + b
>>> a
2
>>> a = 100
>>> a = a + 1
>>> a = 1
>>> a += 1
>>> a -= 1
>>> a *= 1
>>> a %= 1
>>> a /= 1
```

`a = 100`で、メモリ内に`100`を作成し、`a`と`100`を紐付ける.
`a = b`とすると`b`は`a`から`100`の場所を教えてもらう.
つまり`a = 1`と`a`に新たに`1`を教えても, `b`の知っている場所は, `100`.

変数の先頭には、`_`もしくは`alphabet`.  
先頭以外には、数字も使える.

変数に使用できない文字列
```
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
上の文字を使用すると
```
>>> and = 1
  File "<stdin>", line 1
    and = 1
      ^
SyntaxError: invalid syntax
```
と SyntaxError が表示される. 


スペルミスの時などのError
```
>>> aa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aa' is not defined
```

## オブジェクト？データ型？

object 属性とその属性に関する操作をまとめたデータ.

```
>>> divmod(10, 3)
(3, 1)
>>> a = 100
>>> type(a)
<class 'int'>
>>> a = 1.2
>>> type(a)
<class 'float'>
>>> a = 10.1
>>> a2 = int(a)
>>> a2
10
>>> a = '1000'
>>> a2 = int(a)
>>> a2
1000
>>> type(a2)
<class 'int'>
>>> a = 10
>>> a2 = float(a)
>>> a2
10.0
>>> a = '100.0'
>>> a2 = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '100.0'
>>> a2 = float(a)
>>> a2
100.0
>>> a2 = int(a2)
>>> a2
100
>>> a = 'aa'
>>> a2 = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'aa'
```

# 文字列

## 文字列の作成方法

```
>>> first_name = 'taro'
>>> first_name
'taro'
>>> a = "aaa"
>>> '文字列の中に, ""を入れることができる'
'文字列の中に, ""を入れることができる'
>>> number = 1
>>> number_of_string = str(number)
>>> number_of_string
'1'
>>> type(number_of_string)
<class 'str'>
>>> text = """
... おはよう
... こんにちは
... """
>>> text
'\nおはよう\nこんにちは\n'
>>> print(text)

おはよう
こんにちは

>>> text = """おはよう
... こんにちは"""
>>> print(text)
おはよう
こんにちは
>>> text = """\
... おはよう
... こんにちは\
... """
>>> print(text)
おはよう
こんにちは
>>>
```

## 特殊な文字列・文字列どうしの計算

```


```




Mutable : 変更可能な変数の型
Immutable : 内容を変更できない変数の型
Sequence : 添字でアクセスできる

| | Mutable or Immutable | Sequence |
|-|-|-|
| str 型        | Immutable | Sepuence  |
| int,double 型 | Immutable | -         |
| list 型       | Mutable   | Sepuence  |
| tuple 型      | Immutable |  Sepuence |
| dict 型       | Mutable   | -         |
| set 型        | Mutable   | -         |

list 型
```
>>> int_list = [100, 200, 300, 400, 500]
>>> str_list = ["hoge", "fuga", "bar", "foo", "piyo"]
>>> mix_list = [["egg", 100], ["meat", 200], ["fish", 300]]
```

dict 型
```
>>> my_dict = {key1 : value1, key2 : value2}
```
