"""

-Python
-Django  . Recourses

Python Crash Course

Instalacion de Python -
Variables y Tipos de datos -
Strings -
Numbers in Python -
Obtener datos de usuario (input) -
Word replacement exercise -
Listas -
Metodos de listas -
Tuplas -
Funciones -
Return statements -
If statements

Python Exercise 2

Diccionarios -
While loops -
For loops in python
Listas 2d and nested loop
Comentarios
Construyendo calculadora
Try Exept python
Reading files and Writing files
Clases y objetos
Herencia    
Python interpreter
Modules
Introduccion a PIP


"""


"""
Lenguaje rapido de proceso
Machine Learning - Deaarrollo Web - etc

"""


# Nivel 1 - Print()
print('Hello Python!', 'Second Python!')

# Nivel 2 - Variables
# Salvan la informacion en memoria

name = 'Pedro'
print(name)
print(name + ' is has name.')

# Nivel 3 - Strings
# Es un tipo de dato - un string esta compuesto x caracteres
# Metodos Strings -  .upper() - lower() - islower() - supper() - isupper() - len() - index([caracter a buscar]) - .replace([caracter a buscar], [caracter con que se reemplaza])

username = 'mario'
print(username[3])

print(username.upper())
print(username.islower())

# Nivel 4 - Numbers 
#  .srt([dato a cimbertir a string]) - .abs() (abosulete values) - .max([primer numero], [segundo numero]) - .min() - .round([around the value]) - bin([retorn the binar value]) 
# from match import *  [de la clase math importamos todo] -   sqrt([retorna la multiplicacion de los cuadrados])
from math import *

my_number = 32
print(my_number)

print(my_number * 2)

print(abs(-9))

print(sqrt(4546))


# Nivel 5 - Getting users input
#
user = input('Input your user: ')
print('Hello ' + user)