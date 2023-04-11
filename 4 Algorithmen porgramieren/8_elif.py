# Elif (else if)

age = 4

# Wenn <= 6 -> kostenlos
# Wenn > 6 aber <= 60 -> 10€ 
# Wenn > 60 -> 7.50€

if age <= 6:
  print("Du kannst kostenlos in den Zoo!")
elif age > 6 and age <= 60: # funktioniert auch mit or
  print("Du zahlst 10€")
else:
  print("Du zahlst 7.50€")

# Es kann nur immer ein if und else statement geben, jedoch aber unendlich viele elifs

