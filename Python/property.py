class Person:

  def __init__(self, name):
    self.origin_name = name
    self.name = name # setter呼び出し. real_name に格納.

  @property
  def name(self):
    return self.real_name

  @name.setter
  def name(self, value):
    if not value:
      value = 'no name'
    self.real_name = value

person_a = Person('tanaka')
person_b = Person('')

print(person_a.name)
print(person_b.name)
