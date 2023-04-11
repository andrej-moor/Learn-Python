# Listen können sortiert werden
# Zwei Arten der Sortierung -> permanent, temporär (z. B. für eine neue Variable)

animals = ["Bär", "Esel", "Affe", "Zebra","Gepard"]
animals.sort() # nach dem Alphabet sortiert
print(animals)

animals.sort(reverse=True) # umgekehrte Rehenfolge / Boolscher Wert: umgekehrt=ja
print(animals)

# Wenn man die sortierte Liste in einer neuen Variable ausgeben will, also nicht sertören will, kann man dies mit der sorted Funkiton tun (temporäre Sortierung): 
animals_sorted = sorted(animals)
print(f"Sortiert: {animals_sorted}")
print(f"Unsortiert: {animals}")

# Länge von Listen (Anzahl der Elemte)
length = len(animals)
print(f"Längen der List: {length}")