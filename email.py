print("Olá.")
print("Digite [1] para Professor.")
opcao = input("Digite [2] para Estudante.")
opcao = int(opcao)
if opcao == 2:
    ra = input("Digite o RA do estudante:")
    print ("Segue abaixo seus e-mails institucionais:")
    print ("Google:"+ ra +"sp@al.educacao.sp.gov.br")
    print ("Microsoft:" + ra +"sp@aluno.educacao.sp.gov.br")
elif opcao == 1:
    rg = input("Digite o RG do professor (com o digito e o UF):")
    print ("Segue abaixo seus e-mails institucionais:")
    print ("Google:"+ rg +"@prof.educacao.sp.gov.br")
    print ("Microsoft:" + rg +"@professor.educacao.sp.gov.br")