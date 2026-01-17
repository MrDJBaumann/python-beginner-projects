import random

all_rolls = []

print("=" * 40)
print("    DICE ROLLER SIMULATOR")
print("=" * 40)

while True:
    num_dice = int(input("\nHow many dice do you want to roll? "))
    
    results = []
    
    for i in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
        all_rolls.append(roll)
    
    print(f"\nYou rolled: {results}")
    print(f"Total: {sum(results)}")
    
    again = input("\nRoll again? (yes/no): ").lower()
    
    if again != "yes":
        print("\n" + "=" * 40)
        print("STATISTICS:")
        print("=" * 40)
        print(f"Total rolls: {len(all_rolls)}")
        print(f"1's: {all_rolls.count(1)}")
        print(f"2's: {all_rolls.count(2)}")
        print(f"3's: {all_rolls.count(3)}")
        print(f"4's: {all_rolls.count(4)}")
        print(f"5's: {all_rolls.count(5)}")
        print(f"6's: {all_rolls.count(6)}")
        print("=" * 40)
        print("\nThanks for playing!")
        break
