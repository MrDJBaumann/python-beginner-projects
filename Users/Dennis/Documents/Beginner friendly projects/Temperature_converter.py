print('Temperature Converter')
print('=' * 40)
print('\n1. Celsius to Fahrenheit')
print('2. Fahrenheit to Celsius')

choice = input('\nChoose (1 or 2): ')

if choice == "1":
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == "2":
    fahrenheit = float(input('Enter temperatue in Fahrenheit: '))
    celsius = (fahrenheit -32) * 5/9
    print(f'{fahrenheit}°F = {celsius}°C')

else:
    print('EHH! Invalid Choice! Please choose 1 or 2')