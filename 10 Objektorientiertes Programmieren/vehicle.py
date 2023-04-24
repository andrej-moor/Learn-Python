class Vehicle:
  def __init__(self, max_speed, door_count):
    self.max_speed = max_speed
    self.door_count = door_count

  def drive(self):
    print("Das Fahrzeug fährt")
  
class Plane(Vehicle):
  def __init__(self, max_speed, door_count, wing_length):
    super().__init__(max_speed, door_count)
    self.wing_length = wing_length
  def start_landing(self):
    print("Das Flugzeug begint zu landen")

  def drive(self):
    print("Das Fahrzeug fliegt")

