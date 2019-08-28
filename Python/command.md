# 演算




# 文字列

Mutable : 変更可能な変数の型
Immutable : 内容を変更できない変数の型
Sequence : 添字でアクセスできる

| | Mutable or Immutable | Sequence |
|-|-|-|
|: str 型        | Immutable | Sepuence  |
|: int,double 型 | Immutable | -         |
|: list 型       | Mutable   | Sepuence  |
|: tuple 型      | Immutable |  Sepuence |
|: dict 型       | Mutable   | -         |
|: set 型        | Mutable   | -         |

list 型
```
>>> int_list = [100, 200, 300, 400, 500]
>>> str_list = ["hoge", "fuga", "bar", "foo", "piyo"]
>>> mix_list = [["egg", 100], ["meat", 200], ["fish", 300]]
```

dict 型
`>>> my_dict = {key1 : value1, key2 : value2}`
