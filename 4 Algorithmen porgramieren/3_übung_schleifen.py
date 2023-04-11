klasse_a = ["Jan", "Nick", "Maria", "Peter"]
klasse_b = ["Klara", "Jonas", "Hans", "Vladimir"]

for schüler in klasse_a:
  print(schüler)

print("========")
for schüler in klasse_b:
  print(schüler)

print("========")
alle_schüler = klasse_a + klasse_b
for schüler in alle_schüler:
  print(schüler)

print("========")
# Alternativ kann man die einzelenen Elemente durch .append() hinzufügen

for schüler in klasse_b:
  klasse_a.append(schüler)

print(klasse_a)