class Charcter:
  def __init__(self, name):
    self.name = name

  def show_profile(self):
    profile = '名前: {0}, 種族: Charcter'.format(self.name)
    print(profile)

class Monster(Charcter):
  def __init__(self, name):
    super().__init__(name)
    self.hp = 20

  def show_profile(self):
    profile = '名前: {0}, 種族: Monster'.format(self.name, self.hp)

monster_a = Monster('モンスターA')
monster_a.show_profile()

