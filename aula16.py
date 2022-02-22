'''
Formatando valores em Python

:s - Textos (strings)
:d - Inteiros (int)
:f - Numero de ponto flutuante (float)
:. (numero) f- Quantidade de casas decimais (float)
: (caractere)(> ou < ou ^)(Quantidade)(tipo - s, d o f)

> - esquerda
< - Direita
^ - Centro
'''

'''formatar o valor, exemplo diminuir numeros apos a virgula de floats
utilizando o .format
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))

num1 = 10
num2 = 3
divisao = num1 / num2
print(f'{divisao:.2f}')'''

#exemplo para string
'''
print(f'{nome:s}')
'''

# exemplos:
num1 = 1
print(f'{num1:0>10}')  # Imprima numeros 0 a esquerda da variavel, no total 10 casas decimais

num2 = 1150
print(f'{num2:0<10}')  # Imprima numeros 0 a direita da variavel, no total 10 casas decimais

num3 = 2555
print(f'{num3:0^10}')  # Imprima numeros 0 ao centro da variavel, no total 10 casas decimais

num4 = 1150
print(f'{num4:.2f}')  # imprima variavel e mais dois numeros apos a virgula

num5 = 1150
print(f'{num5:0>10.2f}')  # imprima a variaveil com 0 a esqueda, no total 10 casas, e duas apos a virgula

nome = ' Denner IZOLI '
print((50-len(nome)) / 2 )
print(f'{nome:#^50}')  # 50 - quantidade de letras da str dividido por 2, imprima variavel com # ao centro de 50

nome1 = ' Denner IZOLI '
nome_formatado = '{:@>50}'.format(nome1)
print(nome_formatado)  # imprima variavel com @ a esqueda completando um total de 50 casas

nome2 = ' Denner IZOLI '
nome_formatado1 = '{n:0<20}'.format(n=nome2)
print(nome_formatado1)  # imprima variavel com 0 a direita completando um total de 20 casas

nome3 = ' Denner Luiz '
sobrenome = 'Palma'
sobrenome1 = 'Izoli'
nomeformatado2 = '{0:$^50}{2:#^50}'.format(nome3, sobrenome, sobrenome1)  # Utilizando indice, posso escolher qual variavel a ser imppressa
print(nomeformatado2)

nome4 = 'Luiz Denner'
nome4 = nome4.ljust(20,'#')  # ljus justifica o nome ou a variavel a esquerda.
print(nome4)

# funções de str
nome5= 'Luiz denner'
print(nome5.lower())  # tudo minusculo
print(nome5.upper())  # tudo maiusculo
print(nome5.title())  # Primeiras letras maiusculas