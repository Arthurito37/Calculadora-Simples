def primo(): # cria a função primo
    x = input("Digite um número para verificar se ele é primo:") #recebe o número do usuário
    x = int(x) # converte o número do usuário em número inteiro.
    if x < 2: # se o número for menor que dois o programa informará que ele é não é um número primo, pois não é dividido por 1 e por ele mesmo.
        print("O número digitado não é primo.") 
    else: # se for maior, irá dar sequencia no loop
        primo = True # considera inicialmente que é um número primo

        for i in range(2, x // 2 + 1): # fará um calculo onde verifica se a váriavel X é divisível em algum intervalor de 1 até 2
            if x % i == 0: # se o resto da divisão por x for 0 então a váriavel primo é declarada como false e quebra o lop.
                primo = False # primo é declarado como false
                break # sai do loop
        if primo == True: # se o primo continuar sendo true?
                print(x, " é um número primo.") # imprime que o número é primo
        else: # se o primo for false
                print(x, "não é um número primo.") # imprime que o número não é primo

primo() # chama a função primo