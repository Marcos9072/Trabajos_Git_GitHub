lista = [1, 2, 3, 4, 5, 9, 89]
print(f'La longitud de la lista es : {len(lista)}')

suma = 0
for i in lista :
    suma += i
    
print(f'\nLa suma de los valores de la lista es : {suma}')

multiplicacion = 1

for i in lista :
    multiplicacion *= i

print(f'\nLa multiplicacion de los elementos de la lista es : {multiplicacion}')


lista.append(4)
print(f'\nLa longitud actualizada es : {len(lista)}')