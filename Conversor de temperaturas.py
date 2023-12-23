def Celsius():
    print("Você deseja converter uma temperatura que está em celsius.")
    c = input("Qual o valor que da temperatura?")
    c = float(c)
    print("Esse valor vai ser convertido para fahrenheit ou para kelvin?")
    print("Digite 1 para Fahrenheit:")
    y = input("Digite 2 para Kelvin:")
    y =int (y)
    if y == 1:
        c = c*9
        c = c + 160
        c = c/5
        c = str(c)
        print("O valor digitado em Fahrenheit é:", c)
    elif y == 2:
        c = c + 273.15
        c = str(c)
        print("O valor digitado em Kelvin é:", c)
def Fahrenheit():
    print("Você deseja converter uma temperatura que está em Fahrenheit.")
    f = input("Qual o valor que da temperatura?")
    f = float(f)
    print("Esse valor vai ser convertido para Celsius ou para Kelvin?")
    print("Digite 1 para Celsius:")
    y = input("Digite 2 para Kelvin:")
    print (y)
    y = int(y)
    if y == 1:
         f = (f - 32)/9
         f = f * 5
         str (f)
         print("O valor digitado em Celsius é:", f)
    elif y == 2:
        f = (f-32)/9
        f = +273 + (5*f)
        str (f)
        print("O valor digitado em Kelvin é:", f)
def Kelvin():
    print("Você deseja converter uma temperatura que está em Kelvin.")
    k = input("Qual o valor que da temperatura?")
    k = float(k)
    print("Esse valor vai ser convertido para Celsius ou para Fahrenheit?")
    print("Digite 1 para Celsius:")
    y = input("Digite 2 para Fahrenheit:")
    y = int (y)
    if y == 1:
        k = k - 273.15
        k = str(k)
        print ("O valor digitado em Celsius é:", k)
    elif y == 2: 
        k = (k -273.15)/5
        k = k * 9
        k = k + 32
        k = str(k)
        print ("O valor digitado em Fahrenheit é:", k)
print("Olá, você deseja converter uma temperatura, antes de iniciar qual temperatura você já tem o valor?")
print("Digite 1 para Celsius:.")
print("Digite 2 para Fahrenheit:")
print("Digite 3 para Kelvin:")
x = input("Digite o número correspondente:")
x = int(x)
if x > 3:
    print("Digite um dos números correspondentes.")
if x < 1:
    print("Digite um dos números correspondentes.")
if x == 2:
    Fahrenheit()
if x == 1:
    Celsius()
if x == 3:
    Kelvin()
