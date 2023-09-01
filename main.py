# write  a rock-paper-scissors game
import random
def get_user_choice():
    # print("Choose an option:")
    # print("Rock")
    # print("Paper")
    # print("Scissors")
    choice = input("Please input your choice: ")
    choices = {"Rock":1, "Paper":2,  "Scissors":3}
    
    while choice not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid. Please choose again.")
        choice = input("Please input your choice: ")

    return choices[choice]

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "user"
    return "computer"

def main():
    choices = {"Rock":1, "Paper":2,  "Scissors":3}
    comp_choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    wins = 0
    losses = 0
    games_played = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nThe computer chose: {user_choice}")
        print(f"The Player chose: {comp_choices[computer_choice]}")

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
        print("")

        # play_again = input("\nPlay again? (yes/no): ").lower().strip()
        # if play_again != "yes":
        #     break

if __name__ == "__main__":
    main()



