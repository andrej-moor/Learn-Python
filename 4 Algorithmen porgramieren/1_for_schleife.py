# Mit Schleifen kann man z.B. für eine lange liste den gleichen Code ausführen
# Wenn man ein Liste mit 100 Elementen hätte und diese augegen wollte, müsste man 100x den prin()-Elemente schreiben
# Mit einer Schleife kann man mit einer Zeile Code für jedes Element der Liste ausführen

cars = ["Audi", "Bmw", "Vw", "Mercedes"]

# Manuelles ausführen für jeden Wert
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

print("=================")

# Schleife

for car in cars: 
  print(car) # Der print()-Befehl muss eingerükt werden um der Schleife zugehörig zu sein (-> Python arbeitet mit Einrückungen (engl. intendation)

