
'''soma = input('Digite 1 para soma')
subtracao = input('Digite 2 para subtração')
multiplicacao = input('Digite 3 para multiplicação')
divisao = input ('digite 4 para divisão')


input('Ola, esta é minha primeira calculadora em programação, espero que goste, '
      '\n Digite 1 para soma,'
      '\n Digite 2 para subtração,'
      '\n Digite 3 para multiplicação,'
      '\n Digite 4 para divisão. \n ')'''

funcao = input('''Ola, esta é minha primeira calculadora em programação, espero que goste.'
      \n Digite + para soma,
      \n Digite - para subtração,
      \n Digite * para multiplicação,
      \n Digite / para divisão. \n ''')

numero_1 = int(input('Digite o 1 numero da operação '))
numero_2 = int(input('Digite o 2 numero da operação '))

if funcao == '+':
      print(f'{numero_1 + numero_2}')

elif funcao == '-':
      print(f'{numero_1 - numero_2}')

elif funcao == '*':
      print(f'{numero_1 * numero_2}')

elif funcao == '/':
      print(f'{numero_1 / numero_2}')

else:
      print('Voce não digitou um operador valido. ')

