numero1 = input("Digite um número:") #Recebe o primeiro valor
print("Digite a operação desejada:")
print("+ para somar")
print("- para subtrair")
print("* para multiplicar")
print("/ para dividir")
operador = input("")
numero2 = input("Digite um número:") #Recebe o segundo valor
numero1=float(numero1)
numero2=float(numero2)
if "+" in operador: #Soma os dois operadores
    numero1 = numero1 + numero2
if "-" in operador: #Subtrai os dois operadores
    numero1 = numero1 - numero2
if "*" in operador: #multiplica os dois operadores
    numero1 = numero1 * numero2
if "/" in operador: #Divide os dois operadores1
    numero1 = numero1 / numero2

print (numero1)