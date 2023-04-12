animal = {"name" : "Berta", "type" : "Giraffe"}

# Änderung eines KVP
animal["type"] = "Löwe" 
print(animal)

# Hinzufügen eines KVP
animal["partner"] = "Helmut"
print(animal)

# Hinzufügen eines KVP als Dictionary (Verschachtlung)

animal["partner"] = {"name" : "Helmut", "type" : "Giraffe", "hasChildren" : False }
print(animal)

# Spezifische Abfrage
print(animal["partner"]["hasChildren"])