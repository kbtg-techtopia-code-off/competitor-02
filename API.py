from flask import Flask, request, jsonify
import random

app = Flask(__name__)

choices = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Lizard": 4,
    "Spock": 5
}

comp_choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Lizard",
    5: "Spock"
}

wins = 0
losses = 0
games_played = 0

def get_computer_choice():
    return random.randint(1, 5)

def determine_winner(user, computer):
    global wins, losses, games_played

    if user == computer:
        games_played += 1
        return "draw"
    
    winning_combinations = [
        (1, 3), (1, 4),  
        (2, 1), (2, 5),  
        (3, 2), (3, 4),  
        (4, 2), (4, 5),  
        (5, 1), (5, 3)   
    ]
    if (user, computer) in winning_combinations:
        wins += 1
        games_played += 1
        return "user"
    
    losses += 1
    games_played += 1
    return "computer"

@app.route('/play', methods=['POST'])
def play_game():
    global wins, losses, games_played

    data = request.json
    user_choice = choices.get(data.get('playerChoice', '').title())
    
    if not user_choice:
        return jsonify({"error": "Invalid choice"}), 400
    
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    response_data = {
        "computerChoice": comp_choices[computer_choice],
        "winner": winner,
        "wins": wins,
        "losses": losses,
        "gamesPlayed": games_played
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
