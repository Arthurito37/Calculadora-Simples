# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nome = input() #nome do funcionario
salario = float(input()) #salario do funcionario
vendas = float(input()) #vendas do funcionario em dinheiro

vendas = (15*vendas/100) #faz o calculo da comissão das vendas

salario = salario + vendas #soma o salario inicial com a comissão das vendas
print(f"TOTAL = R$ {salario:.2f}")  #imprime na tela o salario final
