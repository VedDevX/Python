import random

Game_list = ["ROCK", "PAPER", "SCISSORS"]

while True:
    player_choice = input("Enter your choice (Rock, Paper, Scissors) or 'quit' to exit: ").upper()
    
    if player_choice == 'QUIT':
        print("Thanks for playing! Goodbye.")
        break
    
    if player_choice not in Game_list:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue
    
    computer_choice = random.choice(Game_list)
    print(f"You chose: {player_choice} and Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a Draw!")
    elif (player_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (player_choice == "PAPER" and computer_choice == "ROCK") or \
         (player_choice == "SCISSORS" and computer_choice == "PAPER"):
        print("Player Won!")
    else:
        print("Computer Won!")
    
    print()  # Print a blank line for better readability
