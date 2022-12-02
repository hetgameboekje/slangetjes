

while True:
  getal_1 = float(input("Voer het eerste getal in: "))
  print("Operators zijn: +, -, *, /")
  operator = input("Voeg een operator toe: ")
  getal_2 = float(input("Voer het tweede getal in: "))

  if operator == "+":
    print("Het antwoord is: " + str(getal_1 + getal_2))
  elif operator == "-":
    print("Het antwoord is: " + str(getal_1 - getal_2))
  elif operator == "*":
    print("Het antwoord is: " + str(getal_1 * getal_2))
  elif operator == "/":
    print("Het antwoord is: " + str(getal_1 / getal_2))
  else:
    print("Ik herken die operator niet, probeer het opnieuw.")

  