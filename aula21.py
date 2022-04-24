# Aula 21 - 37 - Estrutura de repetição em Python

'''
For in Python
Iterando strings com For
Função range (start=0, stop, step=1)
'''

#  utilizando WHILE
'''
texto = 'Python'
c = 0
while c < len(texto):
    print(texto[c])
    c = c + 1
'''
# Utilizando FOR
'''
texto = 'Python'

for n, letra in enumerate(texto):  # função ENUMRATE numero, enumera a cada volta do laço
    print(n, letra)
'''
'''
for numero in range(10):  # a função RANGE, recebe 3 parametros (start=0, stop, step=1) = inicia do zero, e pula de 1 em 1
    print(numero)

'''
# Exemplo
'''
for numero in range(20, 10, -1):
    print(numero)
'''
'''
for n in range(0, 100, 8):
    print(n)

print('###########')

for n in range(100):
    if n % 8 == 0:
        print(n)
'''
'''
texto = 'Python'
ns = ''

for letra in texto:
    if letra == 't':
        ns = ns + letra.upper()
    elif letra == 'h':
        ns = ns + letra.upper()
    else:
        ns = ns + letra
print(ns)
'''

#continue - pula para o proximo laço
#break - termina o laço

texto = 'Python'
ns = ''

 
for letra in texto:
    if letra == 't':
        continue  # neste caso interpreta se quando encontrase a letra t, continue pula para o proximo laço
        ns = ns + letra.upper()
    elif letra == 'h':
        ns = ns + letra.upper()
        break  # pegou a letra h como solicitado porem o break para o restante do codigo - termina o laço
    else:
        ns = ns + letra
print(ns)