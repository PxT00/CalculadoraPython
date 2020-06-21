print("__________          __  .__                    _________        .__               .__          __                ")
print("\______   \___.__._/  |_|  |__   ____   ____   \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________")
print(' |     ___<   |  |\   __\  |  \ /  _ \ /    \  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \ ')
print(" |    |    \___  | |  | |   Y  (  <_> )   |  \ \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/")
print(" |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|   ")
print("           \/                \/            \/          \/     \/          \/                \/                   ")
def main():
 n1 = int(input("Type a number: "))
 n2 = int(input("Another one: "))

 op = input("Choose an operation (+ ADDITION) (- SUBTRACTION) (* MULTIPLICATION) (/ DIVISION) (** POTENTIATION) ")

 soma = n1+n2
 sub = n1-n2
 multi = n1*n2
 div = n1/n2
 pot = n1**n2

 if op == "+":
      print("The result is: ",soma)
 elif op == "-":
      print("The result is: ",sub)
 elif op == "*":
      print("The result is: ",multi)
 elif op == "/":
      print("The result is: ",div)
 elif op == "**":
      print(n1,"to", n2,"is",pot)

while True:
    main()
    if input("Do you want to do another operation? (Y/N)").strip().upper() != 'Y':
        print("See you next time!")
        break





