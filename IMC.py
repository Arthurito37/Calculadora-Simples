massa=input("Digite o peso para calcular o IMC do paciente:")
massa=float(massa)
altura=input("Digite a altura para calcular o IMC:")
altura=float(altura)
imc=(massa/(altura*altura))
imc=float(imc)
if imc < 18.5:
    imc=str(imc)
    print("O índice de massa corporal corresponde a" + imc + """e o paciente se encontra
    com IMC abaixo do peso.""")
elif imc > 18.5 and imc < 24.9:
    imc=str(imc)
    print("O índice de massa corporal corresponde a " + imc + """e o paciente se encontra
    com IMC normal.""")
elif imc > 25 and imc < 29.9:
    imc=str(imc)
    print("O índice de massa corporal corresponde a " + imc + """e o paciente se encontra
    com IMC com sobrepeso""")
elif imc > 30 and imc < 34.9:
    imc=str(imc)
    print("O índice de massa corporal corresponde a " + imc + """e o paciente se encontra
    com IMC com Obesidade grau 1""")
elif imc > 35 and imc < 39.9:
    imc=str(imc)
    print("O índice de massa corporal corresponde a " + imc + """e o paciente se encontra
    com IMC com Obesidade grau 2""")
elif imc > 40:
    imc=str(imc)
    print("O índice de massa corporal corresponde a " + imc + """e o paciente se encontra
    com IMC com Obesidade mórbida""")
