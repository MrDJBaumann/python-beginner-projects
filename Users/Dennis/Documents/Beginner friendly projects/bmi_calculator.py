print("=" * 40)
print("Hi, welcome to the BMI calculator!")
print("=" * 40)

weight = float(input("\n1. Enter your weight: "))
height = float(input("\n2. Enter your height: "))

if height > 3:
    height = height / 100
bmi = weight / (height * height)
print(f"\nYour BMI is: {bmi}")


if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print('Obese')

