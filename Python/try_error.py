your_input = input('put numbers > ')
try:
  number = int(your_input)
  print(10/number)
except ValueError:
  print('[文字が入力されました.]')
except ZeroDivisionError:
  print('[0を入力することは出来ません.]')
except:
  print('[Other Error]')
