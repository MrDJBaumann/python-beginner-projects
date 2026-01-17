print("Multiplication Table Generator")
print("=" * 30)
number = int(input("Enter a number: "))
print("=" * 30) 

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} ={result}")

 