"""
CONDIÇÕES IF, ELIF E ELSE - AULA 9
"""


# IF significa "SE", no exemplo abaixo "SE" TRUE imprima VERDADEIRO, ja estou declarando que e verdadeiro por isso printou o que foi pedido
# ELSE significa "SE NÃO".
# ELIF significa SE NAO, SE.

'''
if True:
    print('Verdadeiro.')

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)
'''

if False:
    print('Verdadeiro.')
    print('Teste dois.')
elif True:
    print('agora é veraddeiro.')
    nome = input('Qual o seu nome?')
    print(f'Seu nome é {nome}.')
elif False:
    print('mais uma verdadeira.')
    print(22 + 22)
else:
    print('Não é verdadeiro.')
    print('Ola')

#  Posso digitar a quantidade de códigos que quiser em cada else ou if, desde que esteja utilizando o mesmo padrao de identação.