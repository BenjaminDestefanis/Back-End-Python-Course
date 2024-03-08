num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
op = input('Enter operator: ')

if op == '+':
    print(int(num1) + int(num2))

elif op == '-':
    print(int(num1) - int(num2))

if op == '/':
    print(int(num1) / int(num2))

if op == '*' or op == 'x':
    print(int(num1) * int(num2))

else:
    print('Invalid data')

