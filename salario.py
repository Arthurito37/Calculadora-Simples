# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
# o valor que recebe por hora e calcula o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

N = int(input()) #recebe o número do funcionário
horasTrabalhadas = int(input()) # recebe o número de horas trabalhadas pelo funcionário
salario = float(input()) #valor da hora trabalhada 

salario = (horasTrabalhadas * salario) #faz o calculo das horas trabalhadas

print(f"NUMBER = {N}") #imprime na tela o numero do funcionario
print(f"SALARY = U$ {salario:.2f}") #imprime na tela o calculo do salario