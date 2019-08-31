def my_range(start, end, step):
  current_number = start
  while current_number < end:
    yield current_number
    current_number += step

for i in my_range(1, 10, 0.1):
  print(i)
