# Lege eine Liste mit Mitarbeitern an. Jeder Mitarbeiter hat einen Namen, eine Berufsbezeichnung und ein Gehalt
# Füge der Liste 5 Mitaarbeiter hinzu 
employees = [
  {"name" : "Jana", "beruf" : "Backerin", "gehalt" : 2_300},
  {"name" : "Tim", "beruf" : "Bauzeichner", "gehalt" : 3_000},
  {"name" : "Andy", "beruf" : "Trainer", "gehalt" : 2_500},
  {"name" : "Klaus", "beruf" : "Maurer", "gehalt" : 2_700},
  {"name" : "Marta", "beruf" : " Buchhalter", "gehalt" : 4_000},
]
# Rechne das Gehalt aller Mitarbiter zusammen (Schleife)

total_salary = 0

for employee in employees:
  total_salary += employee ["gehalt"]
print(total_salary)
