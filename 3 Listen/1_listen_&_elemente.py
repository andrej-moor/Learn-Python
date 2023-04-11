# Listen können im Verhältnis zu Variablen mehrere Werte enthalten auf die man zugreifen kann

animals = ["Affe","Gans","Giraffe","Nashorn"]
            #0      1       2           3
# Die Nummerierung der Liste wird über einen Index abgerufen
# Platz 1 des Index ist immer die 0

print(animals[0]) # Index = 0
print(animals[1])
print(animals[2])
print(animals[3])

# !! Wenn es kein 4 Element gibt, bekommt man eine Fehlermeldung -> List index out of range

# Wenn man das letzte Element einer Liste ausgeben will, kann man mit -1 arbeiten usw.

print(animals[-1])
print(animals[-2]) # oder eben das zweitletzte