# Aula 20 - Iterando Strings com while em Python - passar por cada uma das letras ou strings

#        Indices
#        0123456789........................33
'''
frase = 'o rato roeu a roupa do seu de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    contador = contador + 1

print(nova_string)
'''
'''
frase = 'o rato roeu a roupa do seu de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'i':
        nova_string += 'R'  # Alterando uma letras minusculas para maiusculas
    else:
        nova_string += letra
    contador = contador + 1

print(nova_string)
'''


frase = 'o rato roeu a roupa do seu de roma'  # valor que tem indices = Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input ('Qual a letra que deseja colocar maiuscula: ')

# Iteração <- iterar = Ato de percorrer cada um dos elementos da sua STR ou de seu elemento Iteravel
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper() # Alterando a letra escolhida pelo usuario de minusculas para maiusculas
    else:
        nova_string += letra
    contador = contador + 1

print(nova_string)