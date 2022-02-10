"""
Operadores Lógicos - Aula 11
and
or
not
in
not in
"""

'''a = 2
b = 2
c = 3

a == b and b < c

a == b or b < c

not a == b and not b < c'''

#  Verdadeiro E verdadeiro = Verdadeiro - Verdadeiro E falso = falso OPERADOR AND
#  comparacao1 and comparacao2

#  Verdadeiro ou Verdadeiro - OPERADOR OR
#  comp1 or comp2


'''
a = 2
b = 3

if b > a:
    print('B é maior que A')
else:
    print('A é maior que B')
________________________________
a = 2
b = 3

if not b > a:
    print('B é maior que A')
else:
    print('A é maior que B')

a = 'asdadasd'
b = 0

if not b:
    print('Por favor preencha o valor de A')
___________________________________
nome = 'Denner Izoli'

if 'asd' in nome:
    print('Existe a letra Izo em seu nome')
else:
    print('não existe')
_________________________________


nome = 'Denner Izoli'

if 'oli' not in nome:
    print('Não Existe em seu nome')
else:
    print('Existe')
____________________________________'''

usuario = input('NOME DE USUARIO: ')
senha = input('SENHA DO USUARIO: ')

usuario_bd = 'denner'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha invalidos.')