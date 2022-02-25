# Aula 18 WHILE - estrutura de repetição em Python

'''
While em PYTHON -
Utilizado para realizar ações enquando uma condição for verdadeira

Requisitor: Entender condições e operadores
'''

# WHILE - FOR

# O bloco de códicom com a estrutura em While, é executado enquando for verdadeiro. !!!!

'''1º Exemplo:

while True: #loop infinito
    nome = input('Qual o seu nome? ')
    print(f' Ola {nome}! ')
'''
'''2º Exemplo
x = 0
while x < 5:
    print(x)
    x = x + 1

print('Acabou!')
'''
'''3º Exemplo
x = 0
while x < 10:
    if x == 3:  # quando x for igual a 3 soma + 1. quando executado pula o 3
        x = x + 1
        #continue  # no Continue o codigo continua até finalizar a condição nesse exemplo utilizou para puler o numero 3
        break  #  Quando a palavra break é encontrada ela finaliza o looping.
        #nesse caso o looping fica ativo até x ser igual a 3 e depois finaliza.

    print(x)
    x = x + 1

print('Acabou!')
'''
'''4º Exemplo
x = 0  # coluna 
while x < 10:
# aqui o x aparecera como coluna e o y como linha
    y = 0  # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1  # significa x = x + 1

print('Acabou ! ')
'''

'''5º exemplo'''

while True:
    print()
    num_1 = (input('Digite um numero: '))
    num_2 = (input('Digite outro numero: '))
    operador = input('Digite um Operador: ')
    sair = input('Deseja Sair? [s] sim ou [n] não')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um numero. ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
   # + - / *

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador Invalido!!!')
