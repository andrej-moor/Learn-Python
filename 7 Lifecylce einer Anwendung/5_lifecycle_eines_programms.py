print("Wilkommen zu meiner Vorlesung. Bitte stellt euch vor.")
students = []
user_input =""
while user_input != "quit":
  user_input = input("Wie ist dein Name? ")
  if user_input != quit:
    print(f"Hallo {user_input}")
    students.append(user_input)
print("Wir sind vollzählig. Lasst und beginnen.")

# Es ist kein Problem mehrere While-Schleifen hintereinander laufen zu lassen