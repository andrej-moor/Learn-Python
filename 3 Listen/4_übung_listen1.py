foods = []

foods.append("Salat")
foods.append("Donut")
foods.append("Brötchen")

print(foods)

foods.pop()

print(foods)

foods.insert(1, "Pasta")

print(foods)

print(foods [-1])

foods.sort()
print(foods)

foods.sort(reverse=True)
print(foods)

print("=================")






# 1. erstelle eine Leere List
# (später kommen da deine Lieblinggericht rein)
lieblingsGerichte = []

# 2. weise der List 3 Gerichte zu 
lieblingsGerichte.append("Pasta")
lieblingsGerichte.append("Burger")
lieblingsGerichte.append("Porrige")
print(lieblingsGerichte)

# 3. entferne das letzte Element der Liste
lieblingsGerichte.pop()
print(lieblingsGerichte)

# 4. Füge nach dem ersten Element ein neues Gericht hinzu 
lieblingsGerichte.insert(1, "Döner")

# 5. Gib dir das letzte Element in der List mit print aus
print(lieblingsGerichte)
print(lieblingsGerichte[-1])

# 6. sotieren der Liste
lieblingsGerichte.sort()
print(lieblingsGerichte)

lieblingsGerichte.remove("Pasta")
print(lieblingsGerichte)