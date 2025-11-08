# Simple Calculator
## This program will do idiotic math

print('=' * 30)
print(' Simple Calculator')
print('=' * 30)

num1 = float(input('\nEnter first number: '))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print('\n' + '=' * 30)
print('RESULTS:')
print('=' * 30)
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} ={multiplication}")
print(f"{num1} / {num2} ={division}")
print('=' * 30)
