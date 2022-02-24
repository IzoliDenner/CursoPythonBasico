# aula 17 - Manipulando Strings - indices e fatiamento de strings em Python

'''
Manipulando Strings
* String Indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html - (tipos built-in)
https://docs.python.org/3/library/functions.html - (tipos built-in)
'''

# positivos [012345678]
texto =     'Python S2'
# negativos-[987654321]

print(texto[7])  # a string também é formada pelo indice, ou tem o indice, como o exemplo acima, posso acessa-la desta maneira - positiva

url = 'www.google.com.br/'

print(url[:-1])  # a string também é formada pelo indice, ou tem o indice, como o exemplo acima, posso acessa-la desta maneira - negativa

# no python também podemos usar fatiamentos para criar string ex:

nova_string = texto[:6]  # Aqui estamos puxando a quantidade de string desejadas, quando inicio com : logo entede-se que quer puxar da primeira
nova_string1 = texto[7:]
                         # Sendo assim, preciso somente completar até qual quero puxar. E ao contrario se quero puxar o ultimo
print(nova_string)
print(nova_string1)

nova_string2 = texto [0::2]  # Aqui escolho o primeiro caractere, escolhe até qual e que pule de dois em dois
print(nova_string2)

print (len(texto))

for letra in texto:  # exemplo aulas posteriores
    print(letra)