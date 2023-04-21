# Returnvalues von Funktionene
def build_student(name, major = "Programmieren"): 
  person = {"person_name" : name, "person_major" : major }
  return person

my_person = build_student("Jannick", "Maschienenbau")
print(my_person)
