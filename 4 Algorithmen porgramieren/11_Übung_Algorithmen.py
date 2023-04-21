list_digits = list(range(1,10_001))

list_a = []
list_b = []

for digit in list_digits:
  if digit % 5 == 0:
    list_a.append(digit)
  else:
    list_b.append(digit)
print(list_a)
print(list_b)

print("___________________________")
# Liste mit 10.000 Werten anlegen (1-10.000)

digits = list(range(1,101))

# Zwei leere Listen (list_a) und (list_b) anlegen
list_a = []
list_b = []

# Für jeden Werte in der Liste überprüfüen, ob der Wert duch 5 geteilt werden kann
# Wenn der Wert durch 5 geteilt werden kann -> list_a hinzufügen
# Wenn der Wer nicht durch 5 geteil werden kann -> list_b hinzufügen

for digit in digits:
  if digit % 5 == 0:
    list_a.append (digit)
  else:
    list_b.append(digit)

print(list_a)
print(list_b)



