"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o
valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros
e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os
 ois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

Exemplos de Entrada	        Exemplos de Saída
12 1 5.30
16 2 5.10                   VALOR A PAGAR: R$ 15.50

"""

cod1, un1, valor1 = input().split()
cod2, un2, valor2 = input().split()

cod1 = int(cod1)
cod2 = int(cod2)
un1 = int(un1)
un2 = int(un2)
valor1 = float(valor1)
valor2 = float(valor2)
soma = (un1 * valor1) + (un2 * valor2)
print("VALOR A PAGAR: R$ %0.2f" % soma)


