gehaltsliste =  []

name = ""
gehalt = ""

while True:
  name = input("Gib den Namen ein: \n") 
  gehalt = int(input("Gib das Gehalt ein: \n"))
  gehaltsliste.append({"name" : name, "gehalt" : gehalt})
print(gehaltsliste)

