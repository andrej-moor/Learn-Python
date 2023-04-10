animals = ["Affe","Gans","Giraffe","Nashorn"]
print(animals)

# Austauschen eines Wertes (initialisieren)

animals [1] = "Elefant"
print(animals)

# Man kann ein Element auch entfernen und einen Platzhalter einfügen mit ""
animals = ["Affe","","Giraffe","Nashorn"]
print(animals)
# Eine leere Liste ist auch möglich

animals2 = []
print(animals2)

#Einfügen eines Elements an das Ende einer leere Liste 

animals2.append("Elefant")
animals2.append("Affe")
animals2.append("Gans")
animals2.append("Lurch")
animals2.append("Eidechse")
print(animals2)

# Wenn man in einer Liste eine Element an einer bestmmten Stelle einfügen will nutzt man die Funktion insert
animals2.insert(0, "Löwe")
print(animals2)

# Entfernen vom letzten Element
animals2.pop()
print(animals2)

# Spezifisches Element entfernen
animals2.pop(1)
print(animals2)

removedElement = animals2.pop(1) # man kann somit mit dem Element noch weiter arbeiten
print(removedElement)

del animals2 [1] # das Element wird entgültig gelöscht
print(animals2)

# Wenn man nicht weiß wo im Index ein Wert liegt, so kann man diesen wie folgt entfernen

animals2.remove("Lurch")
print(animals2)
