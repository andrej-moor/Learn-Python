monthly_revenues = [
1000,
2000,
3000,
2500,
1500,
800,
2200,
2600,
3000,
2100,
2000,
1800,
]

for revenue in monthly_revenues:
  print(revenue)

print("==========")

# Was sind die leistungsstärksten Monate (>=2000)?
total = sum(monthly_revenues)
total_best_months = 0 # initialisieren der Variable um sie weiter unten nutzen zu können
total_count_best_months = 0

for revenue in monthly_revenues:
  if revenue >= 2000:
    total_best_months += revenue
    total_count_best_months += 1

print(total)
print(total_best_months)

# Wieviele Monate waren gut?

print(f"Total Revenue: {total}€, total of best months {total_count_best_months}: {total_best_months}€")



