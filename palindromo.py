def checagem (frase):
    frase = frase.replace ("", "").upper()
    if frase == frase[::-1]:
        return True
    else:
        return False
palavra01 = (input("Digite uma palavra:"))
if checagem(palavra01):
    print("Essa palavra é um palindromo.")
else:
    print("Essa palavra não é um palindromo.")
