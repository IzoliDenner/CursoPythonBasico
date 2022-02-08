nome ='Denner Izoli'
idade = 30  # int
altura = 1.78  # float
e_maior = idade > 18  # boolean
peso = 80
imc = peso / (altura ** 2)

'''print(nome ,'tem ', idade, ' anos de idade, com:', altura, 'de altura, maior de idade', e_maior,
      '\n', ' com', peso, 'kilos e seu IMC (indice de massa corporal é de:', imc )'''

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

# {} - utilizo as chaves para chamar diretamente a variavel declarada anteriormente
# para apresentar apenas duas casas decimais por exemplo no "IMC" utilizar : dois pontos a quantidade "2" e f - de float"""

print('\n{} tem {} anos de idade e seu imc é {:.2f}'.format (nome, idade, imc))  # outra maneira de chamar as variaveis .format chamo as variaves em sequencia

print('\n{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))  # desta maneira facilita a manutenção das variaveis posteriormente