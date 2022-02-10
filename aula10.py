"""
Operadores Relacionais - Aula 10
== igualdade
>  maior que
>= maior que ou igual a
<  menor que
<= menor que ou igual a
!= diferente
"""

# variavel = "valor"  # um sinal de igual, atribuindo algo afirmando que uma coisa é igual a outra
# dois sinais de igual, estou perguntando se uma coisa e igual a outra

'''num_1 = 2  # int
num_2 = '2'  # str

print(num_1 == num_2

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 == num_2) # tudo que esta dentro de parenteses e executado primeiro 

print(expressao)

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 > num_2)

print(expressao)

num_1 = 3  # int
num_2 = 2  # int
#                   3 <= 2
expressao = (num_1 <= num_2)

print(expressao)

var_1 = 'Luiz'
var_2 = 'Izoli'

expressao = (var_1 != var_2)

print(expressao)'''

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')

idade = int (idade)

#Limite para pegar emprestimo
idade_menor = 20  #muito jovem
idade_maior = 30  #passou idade


if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} Não pode pegar o emprestimo.')

