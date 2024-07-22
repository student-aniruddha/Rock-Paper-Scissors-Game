#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Rock Paper-Scissors Game

import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or          (user_choice == 'scissors' and computer_choice == 'paper') or          (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose rock, paper, or scissors.")

    # Get user choice
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()

    # Get computer choice
    computer_choice = get_computer_choice()

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Display the results
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

    return result

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        # Display scores
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing! Goodbye!")

# Run the main function
main()

