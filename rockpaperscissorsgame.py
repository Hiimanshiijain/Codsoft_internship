# Import the random module
import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Define the scores for the user and the computer
user_score = 0
computer_score = 0

# Define a function to determine the winner
def determine_winner(user_choice, computer_choice):
    # Use global variables to access and modify the scores
    global user_score
    global computer_score
    # Print the user's choice and the computer's choice
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    # Compare the choices and update the scores accordingly
    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1
    # Print the current scores
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

# Define a function to ask the user if they want to play again
def play_again():
    # Ask the user for their input
    answer = input("Do you want to play another round? (y/n) ")
    # Validate the input
    if answer.lower() in ["y", "yes"]:
        return True
    elif answer.lower() in ["n", "no"]:
        return False
    else:
        print("Invalid input. Please enter y or n.")
        return play_again()

# Define the main function to run the game
def main():
    # Print the welcome message and the instructions
    print("Welcome to Rock, Paper, Scissors!")
    print("To play, enter your choice: rock, paper, or scissors.")
    print("The game will end when either you or the computer reaches 3 wins.")
    # Use a loop to run the game until one of the players reaches 3 wins
    while user_score < 3 and computer_score < 3:
        # Ask the user for their choice and validate it
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        # Determine the winner and update the scores
        determine_winner(user_choice, computer_choice)
        # Ask the user if they want to play again and break the loop if not
        if not play_again():
            break
    # Print the final message and the final scores
    print("Thanks for playing!")
    print(f"Your final score: {user_score}")
    print(f"Computer final score: {computer_score}")
    if user_score > computer_score:
        print("You are the ultimate winner!")
    elif user_score < computer_score:
        print("The computer is the ultimate winner!")
    else:
        print("It's a draw.")

# Call the main function to start the game
main()
