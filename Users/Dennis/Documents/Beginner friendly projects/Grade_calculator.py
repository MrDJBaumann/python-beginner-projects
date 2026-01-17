# Grade calculator
## Getting started

print('=' * 40)
print('         Grade Calculator')
print('=' * 40)

# Get student information
name = input('\nEnter student name: ')
score = int(input('Enter Score (0-100): '))

if score >= 90:
    grade = 'A'
    message = 'Excellent work'
elif score >= 80:
    grade = 'B'
    message = "Good Job!"
elif score >= 70:
    grade = 'C'
    message = 'You passed!'
elif score >= 60:
    grade = 'D'
    message = 'Needs Improvement'
else: 
    grade = 'F'
    message = 'Failed - please study more'

# Results

print('\n' + '*' * 40)
print("Results:")
print("*" * 40)
print(f"Name: {name}")
print(f'Grade: {grade}')
print(f'Comment: {message}')
print("*" * 40)