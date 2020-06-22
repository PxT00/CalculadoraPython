asciiArt = '''
__________          __  .__                    _________        .__               .__          __                
\______   \___.__._/  |_|  |__   ____   ____   \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________
 |     ___<   |  |\   __\  |  \ /  _ \ /    \  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \ 
 |    |    \___  | |  | |   Y  (  <_> )   |  \ \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/
 |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|   
           \/                \/            \/          \/     \/          \/                \/                   
'''
print (asciiArt)

def main():
  firstNumber = int(input("Type a number: "))
  secondNumber = int(input("Another one: "))

  op = input("Choose an operation (+ ADDITION) (- SUBTRACTION) (* MULTIPLICATION) (/ DIVISION) (** POTENTIATION) ")

  sumOperation = firstNumber + secondNumber
  subsubtractionOperation = firstNumber - secondNumber
  multiplicationOperation = firstNumber * secondNumber
  divisionOperation = firstNumber / secondNumber
  potentiationOperation = firstNumber ** secondNumber

  if op == "+":
      print("The result is: ", sumOperation)
  elif op == "-":
      print("The result is: ", subsubtractionOperation)
  elif op == "*":
      print("The result is: ", multiplicationOperation)
  elif op == "/":
      print("The result is: ", divisionOperation)
  elif op == "**":
      print(firstNumber, "to", secondNumber, "is", potentiationOperation)

while True:
    main()
    if input("Do you want to do another operation? (Y/N)").strip().upper() != 'Y':
        print("See you next time!")
        break
