# FizzBuzz 問題
1〜n回まで繰り返し
* 3の倍数は Fizz
* 5の倍数は Buzz
* 15の倍数で Fizz Buzz
* それ以外は 数字
を出力する。


## 解答例
```
for i in range(1, 101)
  if i%15 == 0:
    print('Fizz Buzz', end=' ')
  elif i%5 == 0:
    print('Buzz', end=' ')
  elif i%3 == 0:
    print('Fizz', end=' ')
  elif:
    print(i, end=' ')
```
