# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. 
# Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

A = float(input()) * 2
B = float(input()) * 3
C = float(input()) * 5
MEDIA = (A + B + C) / (2 + 3 + 5)
print (f"MEDIA = {MEDIA:.1f}")