cars = ["Audi", "Bmw", "Vw", "Mercedes"]

counter = 0

for car in cars: # der Doppelpunkt ist wichtig
  counter += 1
  print(f"Auto Nummer {counter} ist {car}")

print ("==============")

print(counter) # da der print()-Befehl nicht zugehörig zur for schleife eingerückt ist, gibt er nur den aufaddierten Wert aus.