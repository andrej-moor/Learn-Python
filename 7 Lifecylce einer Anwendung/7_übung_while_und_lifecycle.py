mitarbeiter_gehalt = {}

while True:
  input_name = input("Gebe den Namen des Mitarbeiters an:\n")
  input_gehalt =  int(input("Gebe das Gehalt des Mitarbeiters an:\n"))
  mitarbeiter_gehalt[input_name] = input_gehalt
  total_employee_count = len(mitarbeiter_gehalt)
  if total_employee_count >=5:
    break
print(mitarbeiter_gehalt)