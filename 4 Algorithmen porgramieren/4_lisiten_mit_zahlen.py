# Listen mit Zahlen
digits = [1,2,3,4,5]

for digit in digits:
  print(digit)

print("==============")

# Bei längeren Zahlenlisten kann man mit der rang()-Funktion arbeiten

digits = list(range(1,11)) # Die letzte Zahl (1001) ist nicht inkludiert
for digit in digits:
  print(digit)

print("==============")
# Die kleinste Zahl ausgeben
digits = list(range(1,6))
smallest_digit = min(digits)
print(smallest_digit)

# Die größte Zahl
highest_digit = max(digits)
print(highest_digit)

# Summe

result = sum(digits)
print(result)

