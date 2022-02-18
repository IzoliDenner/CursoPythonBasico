# 30 exercicios propostos

'''
1 - Faça um programa que peça ao usuario para digitar um numero inteiro. informe se este numero é impar ou par.
Caso o usuario nao digite um numero inteiro, informe que não é um numero inteiro
'''

 # programa - 1
 # 1º Solução
'''
n = input("Digite um numero: ")

if n.isdigit():
    n = int(n)

    if n % 2 == 0:
        print(f"{n} é par")

    else:
        print(f"{n} é impar")

else:
    print("Esse numero nao e inteiro")
'''
# 2º solução checagem invertida

'''numero_int = input('Digite um numero: ')

if not numero_int.isdigit():
    print('Isso não é um numero inteiro.')
else:
    numero_int = int(numero_int)

    if not numero_int % 2 == 0:
        print(f'{numero_int} é impar. ')
    else:
        print(f'{numero_int} ´é par. ')
'''

#2 -Faça um programa que pergunte a hr ao usuario e, baseando se no horario descrito, exiba a saudação aproproiada. Ex
#Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23
'''
hora = input('Digite o horario neste momento: (0-23) ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia !!! ')
        elif hora <= 17:
            print('Boa Tarde !!! ')
        else:
            print('Boa noite !!! ')
else:
    print('Por favor, digite um horario entre 0 e 23')
'''



#3 - Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva:
#"Seu nome é curto; se tiver entre 5 e 6 letras, escreva:"Seu nnome é normal"; maior que 6 escrea: "Seu nome é muito grande".

'''Uma utilização de lógica nas condições
nome = input('Digite seu nome por favor: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é muito curto')

elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é medio: ')

elif tamanho > 6:
    print('Seu nome é muito grande !!!. ')

else:
    print(f'{nome} não é valido como um nome!!!. ')
'''
'''
nome = input('Digite seu nome por favor: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é muito curto')

elif tamanho <= 6:
    print('Seu nome é medio: ')

else:
    print('Seu nome é muito grande !!!. ')
'''
