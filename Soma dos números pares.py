i = 0 #Contador inicia com zero
x = 0
y = 0 #Recebe o resto da divisão
z = 0
print("Este algoritmo irá fazer a soma de todos os números pares presentes de 1 a 100.")
print("Segue abaixo o resultado.")
while i < 100: #enquanto o i for menor que 3 executará o código abaixo
    i = i + 1 # i recebe 1
    y = i % 2 # y é o resto da divisão por 2
    if y == 0: # enquanto o resto da divisão por 2 for 0
        x = x + i # x recebe ele mesmo mais i
        
print (x)   # mostra o valor de x 
