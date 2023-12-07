import random

def get_user_choice():
    """Get user choice for Rock, Paper, or Scissors."""
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game()
