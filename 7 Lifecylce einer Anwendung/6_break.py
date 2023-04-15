print("Even or Odd")
print("Please enter a number:\n") # \n ist ein Zeilenumbruch
print("Enter quit to exit\n")

user_input = ""

while True:

  user_input = input()

  if user_input == "quit":
    print("Auf Wiedersehen!")
    break # break beendet die While-Schleife
  else:
    digit = int(user_input)

    if digit % 2 == 0:
      print("Number is even\n")
    else:
      print("Number is odd\n")
