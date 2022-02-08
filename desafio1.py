nome = 'Denner'
idade = 30
altura = 1.78
peso = 86
ano = 2022
ano_nasc = ano - idade
imc = peso / (altura ** 2)

print('Denner Izoli nasceu no ano de', ano_nasc)
print('O seu Indice de massa corporal é de', imc)

print(f'\n{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O Imc de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')

