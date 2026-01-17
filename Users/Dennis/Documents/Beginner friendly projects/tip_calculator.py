print("=" * 40)
print("      TIP CALCULATOR")
print("=" * 40)

bill = float(input("\nEnter the bill amount: "))
people = int(input("How many people splitting? "))

print("\nChoose tip percentage:")
print("1. 15%")
print("2. 18%")
print("3. 20%")

choice = input("Enter your choice (1, 2 or 3): ")

if choice == "1":
    tip_percent = 0.15
elif choice == "2":
    tip_percent = 0.18
elif choice == "3":
    tip_percent = 0.20  # ← FIXED: was 0.29
else:
    print("Invalid choice! Using 15% as default")
    tip_percent = 0.15

tip_amount = bill * tip_percent
total = bill + tip_amount  # ← FIXED: was tip_percent
per_person = total / people

print("\n" + "=" * 40)  # ← FIXED: was "= * 40"
print("RESULTS:")
print("=" * 40)
print(f'Bill Amount: ${bill:.2f}')
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Per Person: ${per_person:.2f}")
print("=" * 40)
