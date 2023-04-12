
banned_users = {
  "Jannick" : False,
  "Peter" : True,
  "Karl" : False,
}
print(banned_users["Peter"])

# Überprüfung ob es einen Key gibt, wenn nicht das Standartwert

users = {
  "Jannick" : False,
  "Karl" : False,
}
print(users.get("Peter"), False)

