''' AULA-22
listas em Python
Fatiamento
apped, insert, pop, del, clear, extend, +
min, max
range
'''

# lista é um novo tipo de dados a ser utilizado no python
# diferença da lista para a variavel, variavel so tem um valor
# uma lista pode conter varios valores dentro de colchetes
'''
variavel = 'Valor' # O unico valor dentro desta variavel é a String em txto 'VALOR'
lista = [1, 2, 3, 4, 'Denner Luiz', True, 10.5] # Dentro desta lista contem 4 valores diferentes e suporta varios tipos
'''
'''
# 0 1 2 3 4 5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
# - 6 5 4 3 2 1

string = 'ABCDE'
'''
'''
print(string[1]) # acessando o A utilizando variavel, somente a letra correspondente do indice
# a principal caracteristica de usar a lista, que podemos chamar pelo indice uma palavra completa por exemplo e nao somente uma letra
'''
'''lista[5] = 'Qualquer outra coisa.' # modificando o valor dentro da lista, neste caso o valor do indice 5
print(lista[1:4])
print(lista[:3])
print(lista[::-1]) # Não atribui o inicio, ele vai do começo, nao atribui o fim ele vai ate o final, -1 significa começar do fim


print(lista) # imprimo a lista inteira
'''
'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 # concatenando as duas primeiras listas
print(l1)
print(l2)
print(l3)
'''

'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2) # adicionando os valores da lista L2 para a L1
print(l1)
print(l2)
'''

'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend('a') # adicionando o valor A na L1 
print(l1)
print(l2)
'''
'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append('b') # função append inseri o novo valor no final da Lista
print(l2[3])
print(l1)
print(l2)
'''

'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.insert(0,'banana') # adicionou o valor banana no primeiro indice no caso o 0 e os restantes dos valores também são modificados

print(l1)
print(l2)
'''
'''
l2 = [4, 5, 6]
print(l2)
l2.insert(0,'banana')
print(l2)
l2.pop() # Pop, deleta o ultimo valor da lista refenciada
print(l2)
'''

'''
# 0 1 2 3 4 5 6 7 8 - indice
l2 = [1,2,3,4,5,6,7,8,9]# valor
l2.insert(0, 'Banana')
del(l2[3:5]) # DEL serve para remover o trecho que eu quiser da lista
print(l2)
'''
'''
# 0 1 2 3 4 5 6 7 8 - indice
l2 = [1,2,3,4,5,6,7,8,9]# valor
print(l2) # imprimindo a lista como a criei
l2.insert(0, 'Banana')
print(l2) # imprimindo a lista com o valor BANANA que adicionei acima
del(l2[0]) # DEL serve para remover o trecho que eu quiser da lista Neste caso o INDICE 0
print(l2) # imprimindo a lista com o valor excluido acima
'''

'''
# 0 1 2 3 4 5 6 7 8 - indice
l2 = [1,2,3,4,5,6,7,8,9]# valor

print( max(l2)) # imprime o maior valor da minha lista
print( min(l2)) # imprime o menor valor da minha lista
'''

'''
l2 = range(1,10) # maneira de colocar os numeros sem precisar escrever um a um como nos exemplos acima, porem neste caso retor apenas 1 e 10
print(l2)
'''
'''
l2 = list(range(1,10)) # Aqui eu modifico no caso o RANGE que me retornou apenas 1 e 10 no exemplo acima, para LISTA, ou seja valores de 1 a 9
print(l2)
'''
'''
l2 = list(range(0,100,8))
print(l2)
'''
'''
l2 = [1,2,3,4,5,6,7,8,9]# valor

soma = 0
for valor in l2:
 soma = soma + valor

print(soma)
'''
'''
l2 = ['String', True, 10, -20.5]

for elem in l2:
 print(f'O tipo de elem é {type(elem) } e seu valor é {elem}') # utilizando o For para verificar todos os tipos dos valores das listas
'''

secreto = 'perfume'
digitadas = []
chances = 3

while True:
 if chances <= 0:
  print('Voce Perdeu !!')
  break


 letra = input('Digite uma letra: ')

 if len(letra) > 1:
  print('Ahh isso não vale, digite apenas uma letra. ')
  continue

 digitadas.append(letra)


 if letra in secreto:
  print(f'Boaaa, a letra {letra} tem na palavra secreta')
 else:
  print(f'Deu ruim, a letra {letra} não existe na palavra secreta')
  digitadas.pop()


 secreto_temporario = ''
 for letra_secreta in secreto:
  if letra_secreta in digitadas:
   secreto_temporario = secreto_temporario + letra_secreta
  else:
   secreto_temporario = secreto_temporario + '*'

 print(secreto_temporario)

 if secreto_temporario == secreto:
  print(f'Ora ora, parece que temos um Sherlock Holmes por aqui. A palavra secreta era: "{secreto_temporario}" Parabens !!. ')
  break
 else:
  print(f'A palavra secreta está assim: {secreto_temporario}')

 if letra not in secreto:
  chances = chances -1
 print(f'Voce ainda tem {chances} chances.')
 print()