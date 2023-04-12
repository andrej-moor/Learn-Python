cars = ["BMW", "Audi", "Mercedes", "Volkswagen", "Toyota"]

user_car = input("Nach welchem Auto suchst du?")

if user_car in cars:
  print(f"Wir haben einen {user_car} gefunden!")
else:
  print(f"Wir habe einen {user_car} nicht gefunden!")