def Celsius(): #função que transforma celsius em fahrenheit ou kelvin
    print("Você deseja converter uma temperatura que está em celsius.")
    c = input("Qual o valor que da temperatura?") # recebe o valor em celsius
    c = float(c) # declara c como tipo real
    print("Esse valor vai ser convertido para fahrenheit ou para kelvin?")
    print("Digite 1 para Fahrenheit:")
    y = input("Digite 2 para Kelvin:") # recebe do usuário a opção
    y = int (y) # define a opção escolhida como inteiro
    if y == 1: # se o usuário digitar  1 a opção transforma celsious em fahrenheit
        c = c*9
        c = c + 160
        c = c/5
        c = str(c)
        print("O valor digitado em Fahrenheit é:", c)
    elif y == 2: # se o usuario digitar 2 a opção transforma celsius em kelvin
        c = c + 273.15
        c = str(c)
        print("O valor digitado em Kelvin é:", c)
def Fahrenheit(): #função que transforma fahrenheit em celsius ou kelvin
    print("Você deseja converter uma temperatura que está em Fahrenheit.")
    f = input("Qual o valor que da temperatura?") # recebe o valor em fahrenheit
    f = float(f) #declara f como tipo real
    print("Esse valor vai ser convertido para Celsius ou para Kelvin?")
    print("Digite 1 para Celsius:")
    y = input("Digite 2 para Kelvin:")  # recebe do usuário a opção
    print (y)
    y = int(y) # define a opção escolhida como inteiro
    if y == 1: # se o usuário digitar  1 a opção transforma fahrenheit em celsious
         f = (f - 32)/9
         f = f * 5
         str (f)
         print("O valor digitado em Celsius é:", f)
    elif y == 2: # se o usuario digitar 2 a opção transforma fahrenheit em kelvin
        f = (f-32)/9
        f = +273 + (5*f)
        str (f)
        print("O valor digitado em Kelvin é:", f)
def Kelvin():  #função que transforma kelvin em fahrenheit ou celsius
    print("Você deseja converter uma temperatura que está em Kelvin.")
    k = input("Qual o valor que da temperatura?") # recebe o valor em kelvin
    k = float(k) # declara o k como do tipo real
    print("Esse valor vai ser convertido para Celsius ou para Fahrenheit?")
    print("Digite 1 para Celsius:")
    y = input("Digite 2 para Fahrenheit:")  # recebe do usuário a opção
    y = int (y) # define a opção escolhida como inteiro
    if y == 1: # se o usuário digitar  1 a opção transforma kelvin em celsious
        k = k - 273.15
        k = str(k)
        print ("O valor digitado em Celsius é:", k)
    elif y == 2: # se o usuario digitar 2 a opção transforma kelvin em fahrenheit
        k = (k -273.15)/5
        k = k * 9
        k = k + 32
        k = str(k)
        print ("O valor digitado em Fahrenheit é:", k)
print("Olá, você deseja converter uma temperatura, antes de iniciar qual temperatura você já tem o valor?")
print("Digite 1 para Celsius:.")
print("Digite 2 para Fahrenheit:")
print("Digite 3 para Kelvin:")
x = input("Digite o número correspondente:") # recebe a opção do usuário
x = int(x) # declara como x em inteiro
if x > 3: # se o usuário digitar uma opção que seja maior que 3 encerra o programa.
    print("Digite um dos números correspondentes.")
if x < 1: # se o usuário digitar uma opção que seja menor que 1 encerra o programa.
    print("Digite um dos números correspondentes.")
if x == 2: # se o usuário digitar a opção 2 chama a função Fahrenheit()
    Fahrenheit()
if x == 1: # se o usuário digitar a opção 1 chama a função Celsius()
    Celsius()
if x == 3: # se o usuário digitar a opção 3 chama a função Kelvin()
    Kelvin()
