# Number Guessing Game
## Computer picks number, you try to guess it

import random

print('=' * 50)
print('     Number Guessing Game')
print('=' * 50)
print("\nI'm thinking of a number between 1 and 20")
print("Can you guess it?")
print('=' * 50)

# Computer picks a random number
secret_number = random.randint(1, 20)

guess_count = 0
max_guesses = 6


while guess_count < max_guesses:
    guess = int(input(f'\nGuess #{guess_count + 1}: '))
    guess_count = guess_count + 1


    if guess == secret_number:
        print('\n' + '🎉' * 20)
        print('CONGRATULATIONS! YOU WON!')
        print(f"You guess it in {guess_count} tries!")
        print('🎉' * 20)
        break
    elif guess < secret_number:
        print("X Too Low! Try a bigger number")
        remaining = max_guesses - guess_count
        print(f'You have {remaining} guesses left')
    else:
        print("X Too hgih! Try a smaller number")
        remaining = max_guesses - guess_count
        print(f"You have {remaining} guesses left")

if guess != secret_number:
    print("\n" + "😢" * 20)
    print("GAME OVER!")
    print(f"The number was {secret_number}")
    print("Better luck next time!")
    print("😢" * 20)