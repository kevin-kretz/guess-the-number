import random

def print_hint(guess):
    if guess < goal_number:
        print("Higher...")
    else:
        print("Lower...")

goal_number = random.randint(1,100)
guess = int(input("What is your guess? "))
print_hint(guess)

while guess != goal_number:
    guess = int(input("Next guess: "))

    print_hint(guess)

print(f"You did it! The number was {goal_number}")