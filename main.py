import random

goal_number = random.randint(1,100)
current_guess = int(input("What is your guess? "))

if current_guess < goal_number:
    print("Higher...")
else:
    print("Lower...")

while current_guess != goal_number:
    previous_guess = current_guess
    current_guess = int(input("Next guess: "))

    if current_guess < goal_number:
        print("Higher...")
    else:
        print("Lower...")

print(f"You did it! The number was {goal_number}")