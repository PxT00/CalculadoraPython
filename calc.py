n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

op = input("Escolha uma operação matemática (+ ADIÇÃO) (- SUBTRAÇÃO) (* MULTIPLICAÇÃO) (/ DIVISÃO) (** POTENCIAÇÃO)")

soma = n1+n2
sub = n1-n2
multi = n1*n2
div = n1/n2
pot = n1**n2

if op == "+":
    print("A soma é: ",soma)
elif op == "-":
    print("A subtração é: ",sub)
elif op == "*":
    print("A multiplicação é: ",multi)
elif op == "/":
    print("A divisão é: ",div)
elif op == "**":
    print(n1,"elevado à", n2,"é",pot)
