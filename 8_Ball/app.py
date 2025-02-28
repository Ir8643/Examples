from flask import Flask, request, jsonify, render_template
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/8ball', methods=['POST'])
def magic_8_ball():
    answers = [
        "Yes", "No", "Maybe", "Ask again later", "Definitely",
        "Absolutely not", "It is certain", "Don't count on it"
    ]
    
    data = request.get_json()
    question = data.get('question', '')
    answer = random.choice(answers)

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)