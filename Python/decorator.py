def decorator(function):
  print('decorator')
  return function

@decorator #say_hello = decorator(say_hello)
def say_hello():
  print('hello')

say_hello
