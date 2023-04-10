# Werte einer String Variable können verändert mit in print ausgegeben werden. Dies ist zum Beispiel nützlich bei Werten, welche durch den User eingegeben wurde wie z. B. ein "krativ" geschriebener Vorname
first_name = "JaNnIcK" # string

print(f"Hallo {first_name}") # Unveränderte Ausgabe 
print(f"Hallo {first_name.title()}") # Nutzung der .titel()-Funtkione -> Erster buchstabe groß
print(f"Hallo {first_name.upper()}") # Nutzung der .upper()-Funtkione ->Alle Buchstaben Groß
print(f"Hallo {first_name.lower()}") # Nutzung der .lower()-Funtkione ->Alle Buchstaben klein