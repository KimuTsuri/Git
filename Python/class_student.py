members = {}

class Student:
  def __init__(self, name):
    self.name = name
    self.score = {}

  def add_score(self, subject_name, point):
    self.score[subject_name] = pint

  def get_score(self, subject_name):
    return self.score.get(subject_name, 'yet this subject')

members['taro'] = Student('taro')
members['saito'] = Student('saito')
members['tanaka'] = Student('tanaka')

print(members)

