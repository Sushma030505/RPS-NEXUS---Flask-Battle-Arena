from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player = request.json['choice']
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    # WIN CONDITIONS (simple!)
    if player == computer:
        result = 'tie - draw!'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        result = 'win - you beat computer!'
    else:
        result = 'lose - computer beat you!'
    
    return jsonify({
        'player': player.title(),
        'computer': computer.title(),
        'result': result
    })

@app.route('/reset', methods=['POST'])
def reset():
    return jsonify({'status': 'reset complete'})

if __name__ == '__main__':
    app.run(debug=True)
