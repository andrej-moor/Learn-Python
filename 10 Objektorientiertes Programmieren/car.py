class Car: # Eine Klasse ist eine Strucktur dem wie Etwas ist

  def __init__(self, brand, color): # Wenn wir ein Objekt von einer Klasse erstellen, dann nennt sich das instanziieren
    self.brand = brand # Attribute
    self.color = color
    self.speed = 200 # Fixer Wer
    print("Hello World")
  
  def drive(self): # Innenfunktionen der Klasse nennt man Methoden
    print("Das {self.color} Auto fährt!")

  def describe(self):
    print(f"Das Auto hat die farbe {self.color} und die Marke {self.brand}")
