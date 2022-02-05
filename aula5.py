"""
Operadores aritméticos

+ - soma
- - subtração
* - multiplicação
/ - divisão
// - divisão inteira (resustado da divisão é arredondado)
** - exponenciação (um numero elevado a outro, potencia)
% - resto da divisão (ele retorna um módulo, o resto da divisão entre um numero e outro)
()

"""

print('multiplicação (*)', 10 *10 )
print('divisão (/)', 50 / 10 )
print('adição (+)', 10 + 10)
print('subtração (-)', 10 - 5)

print ('\n')

print('multiplicação (*)', 10 * 'A' ) #  inteiro multiplicando uma string, o sinal de multiplicação tbm é utizilado como repetidor

print ('\n')

print('adição (+)', '5' + '5') #  somar duas strings igual a uma concatenação (juntar valores)

print ('\n')

print('Denner' + ' ' + 'Izoli e ele tem 32 anos')

# errado !!! print('Denner' + ' ' + 'Izoli e ele tem' + 32 + 'anos')

print('Denner' + ' ' + 'Izoli e ele tem ' + str(32) + ' anos') #  modificar numero inteiro por string
print ('\n')

print(10/3 , '(/) divisão normal - vai retornar o valor real da divisão')
print(10//3 , '(//) divisão normal - vai arredondadar o valor para um numero inteiro')
print ('\n')

print(2 ** 10, '( ** )retorna o resultado da potenciação')
print ('\n')

print(10 % 3, ' ( % ) faz a divisão e retorna o resto da divisão')
print(30 % 5, ' ( % ) faz a divisão e retorna o resto da divisão nessa caso não tem resto então retorna 0')
print ('\n')

print(5+2*10)
print((5+2)*10, '() utilizo para alterar a precedencia das operações matematicas, igual as regras matematicas')

print(2 + 5 * 3 ** 2 - (23.5 + 23.5))