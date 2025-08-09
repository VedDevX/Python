# Number Guessing Game

# Import the random Module
import random

# Choose the number between  1 - 100 randomly by system
number = random.randint(1, 100)

# Use the for loop
for attempt in range(1, 11):
    # Let the User guess the number 
    player_guess = int(input("Guess the number between 1 - 100. You have 10 attempts: "))
    
    if player_guess == number:
        print(f"Congratulations! You guessed it right in {attempt} attempts.")
        break
    elif player_guess < number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
        
else:
    # This else runs if the for loop completes without a break
    print(f"Sorry! You couldn't guess the number. It was {number}.")