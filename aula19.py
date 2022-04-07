"""
While/Else
contadores
acumuladores
"""
'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador = contador + 1
'''


contador = 1
acumulador = 1

while contador <= 10:  # depois de executar os códigos e quando a expressão passar a ser falsa ele executará o else.
   print(contador, acumulador)

   if contador > 5: # o contador vai até onde é mais que 5, no caso 6 e finaliza o laço não vai para o else.
       break

   acumulador = acumulador + contador
   contador += 1
else:
    print('Cheguei no else.') # não sera exevutado porque a expressão nao passou a ser falsa por conta do break
print('Isso sera executado')

