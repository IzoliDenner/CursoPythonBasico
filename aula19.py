"""
While/Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:  # depois de executar os códigos e quando a expressão passar a ser falsa ele executará o else.
   print(contador, acumulador)

   if contador>5:
       break

   acumulador = acumulador + contador
   contador += 1
else:
    print('Cheguei no else.')
print('Isso sera executado')

