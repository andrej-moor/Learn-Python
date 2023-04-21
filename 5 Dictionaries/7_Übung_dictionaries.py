employees = [
  {"name" : "Andy", "job_title" : "Trainer", "salary" : 25_000},
  {"name" : "Rene", "job_title" : "Prgrammierer", "salary" : 100_000},
  {"name" : "Marta", "job_title" : "Bäckerin", "salary" : 25_000},
  {"name" : "Clemens", "job_title" : "Manager", "salary" : 60_000},
  {"name" : "Ramon", "job_title" : "IT-Suport", "salary" : 35_000}
]

total_salary = 0

for empoloyee in employees:
  total_salary += empoloyee["salary"]

print(total_salary)

print("_________________")
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
