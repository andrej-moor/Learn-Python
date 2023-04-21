cars = []

# Schreibe eine Funtkion die eine Auto zusammenbaut (dictionary)
# und es einer globalen Liste hinzufügt

def create_car(brand, color, price, door_count = 5):
  car  = {"brand": brand, "color" : color, "price" : price, "doors" : door_count}
  cars.append(car)

# rufe diese Funtkion 3x auf um 3 verschiedenen Autos zu erstellen 

create_car("BMW", "Rot", "20_000", "3")
create_car("BMW", "Weiß", "50_000")
create_car("BMW", "Gelb", "30_000")

print(cars)


# das Auto besteht aus Marke, Farbe, Preis und Anzahl der Türen
# wobei Anzahl der Türen stadradmäßig auf 5 gesetzt ist
