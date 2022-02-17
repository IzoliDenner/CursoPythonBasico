#python linguagem de tipagem dinamica - não precisamos mencionar o tipo de dado a ser atribuido na variavel
#python nunca vai converter um tipo de dado em outro para mim

# 28 Documentação e funções built-in

'''num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)

desta maneira, não tenho como verificar por exemplo se o usuario digitar uma string no lugar de um int
o programa vai dar erro, abaixo teremos a solução dsso'''

'''num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

#funções que vão checar se a string pode ser convertida em um numero inteiro
# isnumeri - isdigit - isdecimal
# vão checar somente números e positivos

print(num1.isnumeric())
print(num2.isnumeric())'''


#corrigindo aqui o programa flui melhor, por que mesmo que uma string for digitada o programa nao vai dar um erro
#e sim vao retornar avisando quando nao consegue converter o numero para realizar a conta
'''num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não Pude converter so numeros para realizar contas. ')'''
#uma das soluções

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Não Pude converter so numeros para realizar contas. ')
#outra solução

