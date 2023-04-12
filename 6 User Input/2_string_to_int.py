# !! Input gibt einen Wert vom Datentyp String zurück, mit dem man keine arithmetischen berechnungen durchführen kann
# Deswegen kann man mit der int()- oder float()-Funktion eine String in eine Integer umwandeln
number_as_string = input("Bitte gib eine Zahl ein:")
number_as_int = float(number_as_string) + 10
print(number_as_int)

input("Drücke eine Taste zum beenden.")