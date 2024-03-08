# Listas en python
"""
Caracteristicas:
Secuencia mutable de elementos.
Puede contener elementos de diferentes tipos de datos.
Los elementos se pueden acceder mediante su índice.
Los elementos se pueden modificar, agregar o eliminar.
Se definen utilizando corchetes [].
"""

countris = ['United Kindon', 'EEUU', 'Ghana', 'Nigeria', 'Australia']
user = 'pepe78'
print(countris)
print(countris[2][2])
print(countris[2:])
print(countris[1:3])
print(type(countris))
print(type(user))

#Change a value

countris[0] = 'Mexico'
print(countris)

# Lists Methods

# extend()  -  append() - count() - sort() - reverse() - .copy() - .pop([index que queremos borrar]) - .remove([]) - del - clear
# EJ:  new_list = countris.copy()