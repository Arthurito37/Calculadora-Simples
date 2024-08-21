valores = [0] * 3 # declara a matriz que recebe os valores
valores [0] = float(input("DIGITE A DISTÂNCIA PERCORRIDA")) #recebe o valor responsável pela distância
valores [1] = float(input("DIGITE A QUANTIDADE DE LITROS CONSUMIDA")) #recebe o valor responsável pelos litro consumidos
valores [2] = valores[0]/valores[1] # faz o calculo responsável pela média dos quilômetros percorridos por litro

print(f"FORAM PERCORRIDOS EM MÉDIA {valores [2]} quilômetros por litro")
