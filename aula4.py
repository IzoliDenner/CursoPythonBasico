"""
tipos de dados

str - string 'Assim' ou "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93
bool - booleano/lógico - true/false 10==10

"""

print('Luiz', type('LUIZ'))
print(10, type(10))
print(10.5, type(10.5))
print(10 == 10, type(10 == 10))
print('D' == 'D', type('D' == 'D'))
print('D' == 'l', type('D' == 'l'))

print ('\n')

print ('Luiz', type('luiz'), bool ('luiz'))  # qualquer tipo de dados convertido para bool será true
print ('\n')

print('10', type ('10'), type(int('10')))  # type casting converssão de tipo de dados

print ('\n')

# exercicio

print('Denner', type('Denner'))
print(30, type (30))
print(1.78, type(1.78))
print(30 > 18, type(32 > 18))