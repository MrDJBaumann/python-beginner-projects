print('Password Strength Checker')
print('=' * 30)
password = input('Enter your password:')
length = len(password)
print(f'Length = {length} charachters')
if length < 8:
    strength = "weak"
    print('EH Too short! Password is weak!')
else:
    length = 8
    strength = "Medium"
    print('Good length!')
has_number = False
for char in password:
    if char.isdigit():
        has_number = True

if has_number:
    print('! Has Numbers !')
else:
    print("! Doesn't have nunbers!")
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True

if has_upper:
    print("! Has uppercase letters !")
else: 
    print("! Doesn't have upper case letters !")

print('=' * 30)
if length >= 8 and has_number and has_upper:
    strength = 'Strong'
elif length >=8 and has_number:
    strength = "Medium"
else:
    strength = "Weak"

print(f"Password Strength: {strength}")
print("=" * 30)
