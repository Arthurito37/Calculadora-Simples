def checagem (frase): # cria a função checagem
    frase = frase.replace ("", "").upper() # Remove os espaços em branco da string e a converte para letras maiúsculas.
    if frase == frase[::-1]:  # Verifica se a string é igual à sua inversa (é um palíndromo).
        return True
    else:# Se a string não for um palíndromo.
        return False 
palavra01 = (input("Digite uma palavra:")) # Solicita ao usuário que digite uma palavra e armazena-a na variável palavra01.
if checagem(palavra01):# Chama a função checagem com a palavra inserida pelo usuário e verifica o resultado.
    print("Essa palavra é um palindromo.") # Se a palavra for um palíndromo, imprime essa mensagem.
else:# Se a palavra não for um palíndromo.
    print("Essa palavra não é um palindromo.")
