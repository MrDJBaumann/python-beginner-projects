import random
computer_choice =random.choice(["rock", "paper", "scissors"])

print("=" * 40)
print("Hello, I am your computer. Let's play RPS")
print("=" * 40)

user_choice = input("Choose rock, paper or scissors: ")
print(f"You chose {user_choice}! ")
print(f"I choose {computer_choice}!")

if user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats paper!")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("HA! I win")
