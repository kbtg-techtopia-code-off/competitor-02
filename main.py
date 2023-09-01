# write  a rock-paper-scissors game
import random

def get_user_choice():
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Lizard")
    print("5. Spock")

    choice = input("Please input your choice: ").title()
    choices = {"Rock":1, "Paper":2, "Scissors":3, "Lizard":4, "Spock":5}
    
    while choice not in choices:
        print("Invalid. Please choose again.")
        choice = input("Please input your choice (Rock, Paper, Scissors, Lizard, Spock): ")

    return choices[choice]

def get_computer_choice():
    return random.randint(1, 5)

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    
    winning_combinations = [
        (1, 3), (1, 4),  # Rock crushes Scissors, Rock crushes Lizard
        (2, 1), (2, 5),  # Paper covers Rock, Paper disproves Spock
        (3, 2), (3, 4),  # Scissors cuts Paper, Scissors decapitates Lizard
        (4, 2), (4, 5),  # Lizard eats Paper, Lizard poisons Spock
        (5, 1), (5, 3)   # Spock smashes Rock, Spock smashes Scissors
    ]

    if (user, computer) in winning_combinations:
        return "user"
    return "computer"

def main():
    comp_choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}
    wins = 0
    losses = 0
    games_played = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {comp_choices[user_choice]}")
        print(f"The computer chose: {comp_choices[computer_choice]}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("The winner is: player")
            wins += 1
        elif winner == "computer":
            print("The winner is: computer")
            losses += 1
        else:
            print("It's a draw!")

        games_played += 1
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Games played: {games_played}")
        print("====================================")
        
        # play_again = input("\nPlay again? (yes/no): ").lower().strip()
        # if play_again != "yes":
        #     break

if __name__ == "__main__":
    main()



