"""
Manejo de errores y excepciones en Python
"""

def divide(num1,num2):
    return num1 / num2

try:
    result = divide(5,0)
    print(result) 
except:
    print("You can't divide by 0")



