# Speichere die Werte in einer Liste
gehaltsliste = {} # Geschweifte Klammer -> Dictionary

while True:
  user_input_name = input("Bitte gib den Namen des Mitarbeiters ein: ")
  user_input_gehalt = int(input("Bitte gibt das Gehalt ein: "))

  # Gib die gesamte Liste aus

  gehaltsliste [user_input_name] = user_input_gehalt

  total_employee_count = len(gehaltsliste)
  if total_employee_count >= 3:
    break

print(gehaltsliste)
