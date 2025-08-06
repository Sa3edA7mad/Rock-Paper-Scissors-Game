# Create a simple Rock, Paper, Scissors Game
# Provide a welcome message
# Ask the user to choose rock, paper, or scissors
# Randomly choose rock, paper, or scissors for the computer
# Determine the winner and display the result
# Ask the user if they want to play again
# If yes, repeat the game; if no, show goodbye message and exit the game
# use one fundtion to run the game

# game.py
import random

def determine_winner(user_choice, computer_choice):
    valid_choices = ["rock", "paper", "scissors"]
    
    # Check if inputs are valid
    if not isinstance(user_choice, str) or not isinstance(computer_choice, str):
        return "invalid"
    
    if user_choice not in valid_choices or computer_choice not in valid_choices:
        return "invalid"
        
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

def play_game():
    print("Welcome to the Rock, Paper, Scissors Game!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
# This function encapsulates the entire game logic and can be called to start the game.
# The game will continue until the user decides to stop playing.
# The user can play multiple rounds, and the game will provide feedback on each round.
# The game is simple and easy to understand, making it suitable for all ages.
# The game uses a while loop to keep asking the user for input until they choose to exit.
# The game uses random.choice to simulate the computer's choice, making it unpredictable.
# The game provides clear instructions and feedback to the user, enhancing the user experience.
# The game can be easily extended with more features, such as score tracking or difficulty levels.
# The game is implemented in a single function for simplicity, but it can be modularized if desired.
# The game is a fun way to practice basic programming concepts like loops, conditionals, and user input.
# The game can be run in any Python environment, making it accessible to a wide audience.
# The game is a classic example of a simple interactive program that can be enjoyed by anyone.
# The game can be modified to include more choices or different rules, allowing for creativity and experimentation.
# The game is a great way to introduce beginners to programming concepts in a fun and engaging way.
# The game can be played in a terminal or command line interface, making it easy to run without any additional setup.
# The game can be shared with friends or family, allowing for multiplayer fun if desired.
# The game can be used as a starting point for more complex games or applications
