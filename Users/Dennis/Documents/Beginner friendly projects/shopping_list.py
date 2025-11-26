print("Shopping List Manager")
print("-" * 40)

shopping_list = []

while True:
    print("\n1. Add item")
    print("2. View List")
    print("3. Remove item")
    print("4. Quit")

    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"Done! Added: {item}")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Your list is empty")
        else:
            print("\nYour Shopping list:")
            for item in shopping_list:
                print(f"# {item}")

    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"! Removed: {item}")
        else:
            print("EH! Item not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
