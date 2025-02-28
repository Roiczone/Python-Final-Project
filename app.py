from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Define categories (example)
categories = ["General Knowledge", "Science: Computers", "Science: Gadgets"]

# Store user scores temporarily in memory (for demo purposes)
user_scores = {}

# Open Trivia API URL
OPENTDB_API_URL = "https://opentdb.com/api.php"


@app.route('/')
def index():
    return render_template('index.html', categories=categories)


@app.route('/get_questions', methods=['GET'])
def get_questions():
    category = request.args.get('category')
    difficulty = int(request.args.get('difficulty'))

    # Fetch questions from Open Trivia Database API
    questions = fetch_questions_from_opentdb(category, difficulty)

    return jsonify(questions)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    answers = data['answers']
    difficulty = data['difficulty']
    category = data['category']

    score = calculate_score(answers, difficulty)

    # Save score for user session (temporary storage)
    user_scores[category] = user_scores.get(category, {})
    user_scores[category][difficulty] = score

    # Determine if the user passed (50% or more correct answers)
    passed = score >= len(answers) // 2

    # Generate the appropriate message
    score_message = f"Your Score: {score} ({'You did not pass, so take an easier quiz' if not passed else 'You qualify for a tougher quiz'})"

    next_difficulty = get_next_difficulty(difficulty, passed)

    return jsonify({'score_message': score_message, 'passed': passed, 'next_difficulty': next_difficulty})


def fetch_questions_from_opentdb(category, difficulty):
    # Convert category to Open Trivia's numeric ID
    category_ids = {
        "General Knowledge": 9,
        "Science: Computers": 18,
        "Science: Gadgets": 30
    }

    category_id = category_ids.get(category, 9)  # Default to General Knowledge

    # Open Trivia parameters
    params = {
        'amount': 10,  # Generate 10 questions per round
        'category': category_id,
        'difficulty': ['easy', 'medium', 'hard'][difficulty - 1],
        'type': 'multiple'
    }

    response = requests.get(OPENTDB_API_URL, params=params)
    questions = response.json().get('results', [])

    # Process the questions from Open Trivia
    formatted_questions = []
    for question in questions:
        formatted_questions.append({
            'question': question['question'],
            'options': question['incorrect_answers'] + [question['correct_answer']],
            'answer': question['correct_answer']
        })

    return formatted_questions


def calculate_score(answers, difficulty):
    correct_answers = 0
    for answer in answers:
        if answer['correct']:
            correct_answers += 1

    return correct_answers


def get_next_difficulty(current_difficulty, passed):
    if passed:
        # Increment difficulty if user passes
        if current_difficulty < 3:
            return current_difficulty + 1
    else:
        # Decrement difficulty, but minimum is 1
        if current_difficulty > 1:
            return current_difficulty - 1
    return current_difficulty


if __name__ == '__main__':
    app.run(debug=True)
