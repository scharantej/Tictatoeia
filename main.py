 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    # Get the player's move.
    move = request.form['move']

    # Make the computer's move.
    computer_move = get_computer_move(move)

    # Check if the game is over.
    winner = check_winner(move, computer_move)

    # Render the game page.
    return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner')
def winner():
    # Render the winner page.
    return render_template('winner.html')

@app.route('/loser')
def loser():
    # Render the loser page.
    return render_template('loser.html')

def get_computer_move(move):
    # Get the computer's move.
    computer_move = random.choice(['X', 'O'])

    # Make sure the computer's move is not the same as the player's move.
    while computer_move == move:
        computer_move = random.choice(['X', 'O'])

    # Return the computer's move.
    return computer_move

def check_winner(move, computer_move):
    # Check if the player has won.
    if move == 'X' and computer_move == 'O':
        return 'X'
    elif move == 'O' and computer_move == 'X':
        return 'O'

    # Check if the computer has won.
    if move == 'O' and computer_move == 'X':
        return 'X'
    elif move == 'X' and computer_move == 'O':
        return 'O'

    # The game is a tie.
    return None

if __name__ == '__main__':
    app.run()


main.py


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    # Get the player's move.
    move = request.form['move']

    # Make the computer's move.
    computer_move = get_computer_move(move)

    # Check if the game is over.
    winner = check_winner(move, computer_move)

    # Render the game page.
    return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner')
def winner():
    # Render the winner page.
    return render_template('winner.html')

@app.route('/loser')
def loser():
    # Render the loser page.
    return render_template('loser.html')

def get_computer_move(move):
    # Get the computer's move.
    computer_move = random.choice(['X', 'O'])

    # Make sure the computer's move is not the same as the player's move.
    while computer_move == move:
        computer_move = random.choice(['X', 'O'])

    # Return the computer's move.
    return computer_move

def check_winner(move, computer_move):
    # Check if the player has won.
    if move == 'X' and computer_move == 'O':
        return 'X'
    elif move == 'O' and computer_move == 'X':
        return 'O'

    # Check if the computer has won.
    if move == 'O' and computer_move == 'X':
        return 'X'
    elif move == 'X' and computer_move == 'O':
        return 'O'

    # The game is a tie.
    return None

if __name__ == '__main__':
    app.run()
