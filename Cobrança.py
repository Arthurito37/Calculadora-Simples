nome = input("Digite o nome do cliente:")
distrato = input("O "+ nome + " deve distrato?")
if "S" in distrato:
    distratoValue = input("Digite o valor do distrato:")
    print("""Oi, """ + nome + """. Como vai você?
    Estamos enviando esta mensagem porque ainda não recebemos a 
    confirmação do pagamento do seu distrato no valor total de R$:
    """ + distratoValue + """.  Entre em contato e evite o acúmulo de juros
    e restrições em seu CNPJ. Atenciosamente - Departamento Financeiro Monitor contábil.""")
if "N" in distrato:
    setup = input("O " + nome + " deve implantação?" )
    if "S" in setup:
        setupValue = input("Digite o valor da implantação: ")
        setupValue = float(setupValue)
        setupParcela = input("Qual parcela o cliente está inadimplente?")
        setupParcela = int(setupParcela)
        mmr = input("O " + nome + " deve mensalidade? ")
        if "S" in mmr:
            mmrMonths = input("Quantas mensalidades? ")
            mmrMonths = int(mmrMonths)
            mmrValue = input("Qual o valor da mensalidade? ")
            mmrValue = float(mmrValue)
            mmrTotal = mmrMonths * mmrValue
            mmrTotal = float(mmrTotal)
            setupValue = str(setupValue)
            setupParcela = str(setupParcela)
            mmrMonths = str(mmrMonths)
            mmrValue = str(mmrValue)
            mmrTotal = str(mmrTotal)
            print ("""Oi,""" + nome + """. Como vai você? Estamos enviando esta mensagem
            porque ainda não recebemos a confirmação do seu pagamento referente a """ + setupParcela + """º
            da implantação no valor de R$:""" + setupValue+ """. Também não recebemos a confirmação do 
            pagamento referente a(s) mensalidades no valor total de R$: """ + mmrTotal + """. Você teve algum
            imprevisto ou precisa de um novo boleto? Entre em contato e evite o acúmulo de juros
            e bloqueio da ferramenta. Atenciosamente - Departamento Financeiro Monitor contábil.""")
        if "N" in mmr:
            print("""Oi """ + nome + """. Como vai você? 
            Estamos enviando esta mensagem porque ainda não recebemos a confirmação do
            seu pagamento referente a """ + setupParcela + """ parcela da implantação no valor total de
            R$: """ + setupValue + """. Você teve algum imprevisto ou precisa de um novo boleto? 
            Entre em contato e evite o acúmulo de juros e bloqueio da ferramenta.""")
    if "N" in setup:
        mmr = input("O " + nome + " deve mensalidade? ")
        if "S" in mmr:
            mmrMonths = input("Quantas mensalidades? ")
            mmrMonths = int(mmrMonths)
            mmrValue = input("Qual o valor da mensalidade? ")
            mmrValue = float(mmrValue)
            mmrTotal = mmrMonths * mmrValue
            mmrTotal = float(mmrTotal)
            mmrMonths = str(mmrMonths)
            mmrValue = str(mmrValue)
            mmrTotal = str(mmrTotal)
            print ("""Oi, """+ nome +""". Como vai você?
            Estamos enviando esta mensagem porque ainda não recebemos
            a confirmação do pagamento de alguma(s) mensalidade(s) no valor 
            total de R$: """+ mmrTotal +""". Entre em contato e evite o acúmulo de juros
            e bloqueio da ferramenta e restrições em seu CNPJ.
            Atenciosamente - Departamento Financeiro Monitor contábil.""")

