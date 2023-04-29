import random

print("Welcome to Rock-Paper-Scissors game!\n")

moves = ["rock", "paper", "scissors"]

while True:
    player_move = input("Enter your move (rock/paper/scissors): ")
    player_move = player_move.lower()
    
    if player_move not in moves:
        print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.\n")
        continue
    
    computer_move = random.choice(moves)
    
    print("You played", player_move)
    print("Computer played", computer_move)
    
    if player_move == computer_move:
        print("It's a tie!\n")
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        print("You win!\n")
    else:
        print("Computer wins!\n")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no":
        break
    
print("Thanks for playing Rock-Paper-Scissors game!")
