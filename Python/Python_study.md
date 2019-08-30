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

### 空文字列
```
>>> my_str = ' '
>>> type(my_str)
<class 'str'>
```

### エスケープシーケンス
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

## 文字列の属性の確認
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


# list型
```
>>> int_list = [100, 200, 300, 400, 500]
>>> str_list = ["hoge", "fuga", "bar", "foo", "piyo"]
>>> mix_list = [["egg", 100], ["meat", 200], ["fish", 300]]
```
listとは、objectを順番に格納する入れ物

```
>>> my_str = 'Python, Rubby'
>>> my_list = my_str.split(',')
>>> my_list
['Python', ' Rubby']
```
自分でリストを作ってみる
```
>>> my_list = [1, True, False, 'Hello']
```
空のリストに格納する
```
>>> my_list = []
>>> my_list = list()
>>> my_list.append('Jiro')
>>> my_list.append('Taro')
>>> my_list
['Jiro', 'Taro']
```
他の文字列をリストに格納する
```
>>> my_list = list('Python')
>>> my_list
['P', 'y', 't', 'h', 'o', 'n']
```
## listを操る
```
>>> numbers = [1, 2, 3, 4, 5]
>>> len(numbers)
5
>>> sum(numbers)
15
>>> max(numbers)
5
>>> min(numbers)
1
>>> numbers = [1, 2, 3]
>>> numbers1 = [1, 2, 3]
>>> numbers2 = [4, 5, 6]
>>> numbers3 = numbers1 + numbers2
>>> numbers3
[1, 2, 3, 4, 5, 6]
```
### insert関数
```
>>> numbers.insert(1, 1.5)
>>> numbers
[1, 1.5, 2, 3, 4, 5]
```
### pop関数
```
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers.pop(0)
1
>>> numbers
[2, 3, 4, 5]
>>> numbers.pop()
5
>>> numbers
[2, 3, 4]
>>> deleted = numbers.pop()
>>> deleted
4
```
### remove関数
```
>>> my_list = ['a', 't', 'u']
>>> my_list.remove('t')
>>> my_list
['a', 'u']
```
### index関数 in関数 count関数

```
>>> numbers = [1, 2, 3]
>>> numbers.index(2)
1
>>> 1 in numbers
True
>>> 9 in numbers
False
>>> numbers.count(1)
1
>>> numbers.count(9)
0
```

### join関数

```
>>> parts = ['今日は', 'とても', 'いい天気']
>>> poem = '\n'.join(parts)
>>> print(poem)
今日は
とても
いい天気
```

### sort関数

```
>>> numbers = [5, 3, 4, 7, 9, 8]
>>> numbers.sort()
>>> numbers
[3, 4, 5, 7, 8, 9]
>>> numbers.sort(reverse=True)
>>> numbers
[9, 8, 7, 5, 4, 3]
```

# tuple型

```
>>> my_tuple = ()
>>> my_tuple = tuple()
>>> my_tuple = (1, True, False, 'Hello')
>>> my_tuple = 1, True, False, 'Hello'
>>> type(my_tuple)
<class 'tuple'>
>>> my_tuple
(1, True, False, 'Hello')
```

```
>>> one_tuple = 'Python'
>>> one_tuple
'Python'
>>> type(one_tuple)
<class 'str'>
>>> my_tuple = 'Python', 'Ruby'
>>> my_tuple[0]
'Python'
>>> type(my_tuple)
<class 'tuple'>
```

注意！tupleには`append`メソッドがない.

## tupleとlistの違い
tupleを使うメリット
- 中身が変更されないことが保証されている.
- 辞書型のオブジェクトのキーとして利用できる.(Immutableだから)

# dict型

list型 : 1に対してobjectを紐付ける  
dict型 : 名前に対してobjectを紐付ける  
通常の辞書型は、順番を持たない！
```
>>> my_dict = {key1 : value1, key2 : value2}
```
空の辞書
```
>>> source = {}
>>> source = dict()
```
辞書型に変換
```
>>> names = [['さとう', '太郎'],['たなか', '次郎']]
>>> names_dict = dict(names)
>>> names_dict
{'さとう': '太郎', 'たなか': '次郎'}

>>> a = ['ab', 'cd', 'ef']
>>> dict(a)
{'a': 'b', 'c': 'd', 'e': 'f'}
```

## dictを操る

### get
```
>>> score = {}
>>> science = score.get('science', 'no data')
>>> science
'no data'
>>> 
>>> score['science'] = 100
>>> science = score.get('science', 'no data')
100
```
二番目の引数をいれなければ, データがない場合`None`となる. 

### update
辞書に追加

```
>>> band_members = {'ギター' : 'さとう', 'ベース' : 'よしだ'}
>>> new_members  = {'ドラム' : 'たなか'}
>>> band_members.update(new_members)
>>> band_members
{'ギター': 'さとう', 'ベース': 'よしだ', 'ドラム': 'たなか'}
```
### pop
辞書の削除
```
>>> band_members = {'ギター' : 'さとう', 'ベース' : 'よしだ'}
>>> deleted = band_members.pop('ギター')
>>> deleted
'さとう'
>>> band_members
{'ベース': 'よしだ', 'ドラム': 'たなか'}
```

### setdefault
```
>>> base = band_members.setdefault('ベース', '滝沢')
>>> base
'よしだ'
>>> guitar = band_members.setdefault('ギター', '滝沢')
>>> guitar
'滝沢'
```

# set型

```
>>> my_set = {1, 2, 3}
>>> my_set
{1, 2, 3}
>>> type(my_set)
<class 'set'>
>>> my_set = set()
```
listからsetに変換
```
>>> my_list = [1, 2, 3, 3]
>>> my_set = set(my_list)
>>> my_set
{1, 2, 3}
```
setは, 重複しない.

## 集合

```
>>> mutuble = {'list', 'dict', 'set'}
>>> immutable = {'str', 'number', 'tuple'}
>>> sequence = {'list', 'tuple', 'str'}
>>> mutable & sequence
{'list'}
>>> mutuble | sequence
{'tuple', 'list', 'set', 'dict', 'str'}
>>> mutuble - sequence
{'dict', 'set'}
>>> mutuble ^ sequence
{'tuple', 'dict', 'set', 'str'}
```

Mutable or Imutable, Sequence まとめ  

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

# 条件分岐

## if, else
```
names = ['田中', '佐藤', '吉田']

if '田中' in names:
  print('田中さんがいました')
else:
  print('田中さんはいません')

if '滝沢' in names:
  print('滝沢さんがいました')
else:
  print('滝沢さんはいません')

print('処理を終了します')
```
実行結果
```
$ python3 sample_01.py
田中さんがいました
滝沢さんはいません
処理を終了します
```

## 比較演算子

| 演算 | 処理 |
|-|-|
|　`a == b`　| aとbが等しければ, `True` |
|　`a =! b`　| aとbが等しくなければ, `True` |
|　`a < b`　 | aがbより小さければ, `True` |
|　`a <= b`　| aがb以下ならば, `True`(等しくても`True`) |
|　`a > b`　 | aがbより大きければ, `True` |
|　`a >= b`　| aがb以上ならば, `True`(等しくても`True`) |
|　`a in b`　|  |

## bool演算子

| 演算 | 処理 |
|-|-|
| `式A and 式B` | 式Aと式Bが共に`True`ならば, `True` |
| `式A or 式B`  | 式A, 式Bどちらかが`True`ならば, `True` |
| `not 式A`| 式Aが`False`ならば, `True` |

## Falseと評価されるobject

* 空文字列 `''`
* 空タプル `（）`
* 空リスト `[]`
* 空辞書 `{}`
* 空セット `set()`
* 整数の0, 浮動小数点数の0.0
* False
* None

# 繰り返し処理

## for文
```
names = ['田中', '佐藤', '吉田']

for name in names:
  print(name)
```
実行結果
```
$ python3 sample_02.py 
田中
佐藤
吉田
```

### 便利なforループ
演習1
```
names = ['田中', '鈴木', '佐藤']
index = 0
for name in names:
  massage = '{0}番目 {1}'.format(index, name)
  print(massage)
  index +=1
```
組み込み関数`enumerate`を用い, pythonらしい書き方に変更してみる.
```
names = ['田中', '鈴木', '佐藤']
for index, name in enumerate(names):
  massage = '{0}番目 {1}'.format(index, name)
  print(massage)
```

演習2
```
foods = ['納豆', 'ヨーグルト', 'チャーハン']
juices = ['コーラ', 'コーヒー', 'カフェラテ']
for food, juice in zip(foods, juices):
  print(food, juice)
```
リストを複数使用する場合は, 組み込み関数`zip`を使用すると簡単に書ける. 
`zip`関数の使用は短い方に合わせる.  

## range関数
指定回数の繰り返し
```
for i in range(1, 101, 2):
  print(i)
```
1〜100まで2足しあげて繰り返し.  
101番目は含まない.  
実行結果
```
$ python3 sample_03.py
1
3
5  
(省略)  
45
99
```
リスト型にrangeで詰めていく.
```
my_list = list(range(1,101)
```
パフォーマンスのためlist型に直接詰めていくことはできない.

## while文
```
flag = True
while flag:
  user_input = input()
  if user_input == 'exit':
    flag = False
```
### break
```
while True:
  user_input = input()
  if user_input == 'exit':
    break
```
### continue
```
while True:
  user_input = input()
  if user_input == 'exit':
    break
  elif user_input == 'skip':
    continue
  massage = 'あなたの入力は, {0}でした'.format{user_input}
  print{massage}
```
### else
```
names = ['田中太郎', '佐藤次郎', '鈴木三郎']
for name in names:
  if names.endswith('三郎'):
    print('います')
    break
else:
  print('いません')
```

# 内包表記
## 基本的な内包表記
```
numbers = [1,5,6,11,3,5,7]
squares = []
for num in numbers:
  squares.append(num**2)
print(squares)
```
リスト内包表記へ
```
numbers = [1,5,6,11,3,5,7]
squares = [num**2 for in numbers]
print(squares)
```
## 文字列のリストの内包表記
一文字ずつ出力
```
words = ['python', 'django']
one_words = [char for word in words for char in word]
print(one_words)
```

## 1〜10までのサンプルを作成する
```
numbers = [x for x in range(1,11)]
print(numbers)
```
偶数サンプル
```
even_numbers = [x for x in range(1,11) if x%2 == 0]
print(even_numbers)
```
奇数サンプル
```
odd_numbers = [x for x in range(1,11) if x%2 == 1]
print(odd_numbers)
```

## 二次元配列を作成する
```
tuble = [[] for _ in range(1, 10)]
print(tuble)
```
99の表を作ってみる.
```
tuble = [[x*y for in range(1,10)] for y in range(1, 10)]
print(tuble)
```

# ファイルを扱う

## ファイルの書き込み
```
text = ***おはよう
こんにちは
こんばんわ***

# ファイルを書き込むためのobject
file = open('hello.txt', 'w', encoding='utf-8')

# ファイルに書き込み
file.write(text)

# ファイルを閉じる
file.close()
```
モード`a` : ファイルへの追記
```
file = open('hello.txt', 'a', encoding='utf-8')
```
モード`x` : ファイルがない場合だけ書き込み, ある場合は`exit`
```
file = open('hello.txt', 'a', encoding='utf-8')
```
モード`wt` : バイナリモード
```
file = open('a.png', 'wt')
```
with文でファイルの書き込み  
ファイルの閉じ忘れ防止になる.
```
text = ***おはよう
こんにちは
こんばんわ***

# 処理が終われば自動的にファイルを閉じる.
with open('hello.txt', 'w', encoding='utf-8') as file:
 file.write(text)
```

## ファイルの読み込み
```
file = open('hello.txt', 'r', encoding='utf-8)
src = file.read()
print(src)
```
with文でファイルの読み込み
```
with open('hello.txt), 'r', encoding='utf-8) as file:
 for line in file:
   print (line, end='')
```
printは自動的に改行されるため, 空文字列`end=''`を入れている.

# 関数

* 繰り返し出てくるコードを再利用する.
* 大きいプログラムを分割する.
* 他の開発者に, 便利な機能を提供する.


