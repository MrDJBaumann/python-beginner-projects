print('=' * 40)
print('Bulgarian Grade Calculator')
print('=' * 40)

name = input('\nEnter your name: ')
your_grade = float(input('\nEnter your grade: '))
total_points = float(input('\nEnter total possible points: '))

grade = (your_grade / total_points) * 6
grade = round(grade, 2)

print(f"\n{name}, your grade is: {grade}")

if grade >= 5.50:
    print("Rating: Excellent (Отличен)")
elif grade >= 4.50:
    print("Rating: Very Good (Много добър)")
elif grade >= 3.50:
    print("Rating: Good (Добър)")
elif grade >= 3.00:
    print("Rating: Satisfactory (Среден)")
elif grade >= 2.00:
    print("Rating: Poor (Слаб)")
else:
    print("Rating: Fail (Недостатъчен)")