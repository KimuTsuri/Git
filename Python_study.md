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

## 特殊な文字列

空文字列
```
>>> my_str = ' '
>>> type(my_str)
<class 'str'>
```

エスケープシーケンス
 - `\t`
```
>>> hello = 'Hello\tWorld'
>>> print(hello)
Hello   World
```
 - `\n`(改行)
```
>>> print(hello)
>>> print(text)
Hello
World
```
 - エスケープシーケンスを表示させる
```
>>> text = 'Hello\\n'
>>> print(text)
Hello\n
```

文字列の属性の確認
```
>>> my_str = 'Hello'
>>> dir(my_str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## 文字列の便利なmethod

### format

```
>>> fmt = '私の名前は{}です'
>>> name = '太郎'
>>> fmt.format(name)
'私の名前は太郎です'

>>> fmt = '私の名前は{}{}です'
>>> fmt.format('さとう', '太郎')
'私の名前はさとう太郎です'

>>> fmt = '{last_name} {first_name}'
>>> fmt.format(last_name='さとう', first_name='太郎')
'さとう 太郎'
```

### fstrings

```
>>> last_name = 'さとう'
>>> first_name = '太郎'
>>> f'{last_name} {first_name}'
'さとう 太郎'
```

昔からの書き方
```
>>> name = '太郎'
>>> '私の名前は%sです' % name
'私の名前は太郎です'
```

### split

```
>>> languages = 'Python, Ruby, PHP, Perl'
>>> languages.split(',')
['Python', ' Ruby', ' PHP', ' Perl']
```

### separator

```
>>> lang_list = languages.split(',')
>>> separator = ','
>>> separator.join(lang_list)
'Python, Ruby, PHP, Perl'
>>> ','.join(lang_list)
'Python, Ruby, PHP, Perl'
```

### replace

```
>>> poem = '今日はとてもいい天気でした'
>>> poem.replace('今日', '昨日')
'昨日はとてもいい天気でした'
```


### count

```
>>> text = 'Hello, Hello, Hello'
>>> text.count('Hello')
3
```

### startswith

```
>>> name = 'さとう太郎'
>>> name.startswith('さとう')
True
>>> name.startswith('よしだ')
False
```

### endswith

```
>>> name = 'さとう太郎'
>>> name.endswith('太郎')
True
```

### find

```
>>> text = 'Hello World'
>>> text.find('Hello')
0
>>> text.find('H')
0
>>> text.find('jjjj')
-1
```
0から始まり, 見つからなければ`-1`.

### index

```
>>> text = 'Hello World'
>>> text.index('Hello')
0
>>> text.index('jjjj')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

### in 演算子

含まれていれば`True`, 含まれていなければ`False`

```
>>> name = 'さとう太郎'
>>> '太郎' in name
True
>>> 'たろう' in name
False
```

### strip

```
>>> text = '    Hello World     '
>>> text.strip()
'Hello World'
>>> text.lstrip()
'Hello World     '
>>> text.rstrip()
'    Hello World'
```

## シーケンス型としての文字列操作

文字列から文字を取り出す
```
>>> text = 'あいうえお'
>>> text[0]
'あ'
>>> text[1]
'い'
>>> text[-1]
'お'
>>> text[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> text_len = len('あいうえお')
>>> text_len
5
>>> text[text_len-1]
'お'
```

スライス処理
```
>>> text[1:4]
'いうえ'
>>> text[1:]
'いうえお'
>>> text[:100]
'あいうえお'
```

ステップ指定
```
>>> text[::2]
'あうお'
>>> text[1:4:2]
'いえ'
>>> text2 = text[1:4]
>>> text2[::2]
'いえ'
```


# list, tuple


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

## list
```
>>> int_list = [100, 200, 300, 400, 500]
>>> str_list = ["hoge", "fuga", "bar", "foo", "piyo"]
>>> mix_list = [["egg", 100], ["meat", 200], ["fish", 300]]
```

## dict
```
>>> my_dict = {key1 : value1, key2 : value2}
```


