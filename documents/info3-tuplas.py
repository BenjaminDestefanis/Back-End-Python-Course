# tuplas
"""
Caracteristicas:
Secuencia inmutable de elementos.
Puede contener elementos de diferentes tipos de datos.
Los elementos se pueden acceder mediante su índice.
Los elementos no se pueden modificar, agregar o eliminar una vez que la tupla está creada.
Se definen utilizando paréntesis ().
"""


numbers = (1,2,3,4,2,2)
strings = ('home','earth','land','earth')

list_fruts = ['banana', 'Pear', 'Apple', 'Orange']

print(numbers, strings)
print(type(numbers))

# numbers[2] = 8 # Lanza  error
# count() - index() - len() - max() - min() 
# max - min retornan el elmento maximo y el elmento minimo de la tupla
# sorted() - retorna una nueva
print(numbers.count(2)) # Retorna el numero de veces que el elemnto esta en la tupla
print(strings.index('earth')) # retorna el numero de indice si encuentra el elemtneto
print(len(list_fruts))