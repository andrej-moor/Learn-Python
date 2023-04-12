# Iterieren durch ein Dicticionary

students = {
  "Andy" : 36335,
  "Perter" : 37548,
  "Jana" : 97345,
}

# Key + Value
for name , matrikelnummer in students.items():
  print(f"Name: {name} und Matrikelnummer: {matrikelnummer}")

# Nur Key
for key in students.keys():
  print(f"Key: {key}")

# Nur Value
for value in students.values():
  print(f"Value: {value}")

# Liste Loopen
students = [
  {"name" : "Jannick", "age" : 28 , "matricl_nummber" : 97835},
  {"name" : "Andy", "age" : 23 , "matricl_nummber" : 93564},
  {"name" : "Henry", "age" : 35 , "matricl_nummber" : 93645},
]

# for in for
for student in students:
  # key & value sind variablen
  for key, value in student.items():
    print(f"Key: {key} und Value: {value}")



