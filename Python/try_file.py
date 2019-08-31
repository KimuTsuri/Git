try:
  file = open('hello.txt', 'x', encoding='utf-8')

except FileExistsError:
  print('ファイルがすでに存在しています.')

else:
  file.write('hello') # fileがなかった時の通常動作を入れる.

finally:
  file.close() #fileを閉じる.
