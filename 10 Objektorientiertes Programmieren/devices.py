class Device:
  def __init__(self, name):
    self.name = name

  def main_funcionality(self):
    print(("Die Superklasse hat keine Funktion"))

class Vacuum_Cleaner(Device):
  def __init__(self, name, clean_power):
    super().__init__(name)
    self.clean_power = clean_power
  def main_funcionality(self):
    print(("Der Staubsauger saugt."))

class Mixer(Device):
  def __init__(self, name, mix_power):
    super().__init__(name)
    self.mix_power = mix_power
  def main_funcionality(self):
    print(("Der Mixer mixt."))


