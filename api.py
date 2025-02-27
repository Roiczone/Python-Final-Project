from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Added More Questions for Python and C++
question_bank = [
    # Java Difficulty 1 (3 Questions)
    {"question": "What is the keyword to declare a variable in Java?", "options": ["int", "var", "let"],
     "difficulty": 1, "points": 1, "language": "Java", "correct_answer": "int"},
    {"question": "Which data type is used to store text in Java?", "options": ["char", "String", "Text"],
     "difficulty": 1, "points": 1, "language": "Java", "correct_answer": "String"},
    {"question": "What symbol is used for comments in Java?", "options": ["//", "#", "/*"], "difficulty": 1,
     "points": 1, "language": "Java", "correct_answer": "//"},

    # Java Difficulty 2 (3 Questions)
    {"question": "What keyword is used to create a subclass in Java?", "options": ["extends", "inherits", "sub"],
     "difficulty": 2, "points": 1, "language": "Java", "correct_answer": "extends"},
    {"question": "Which of these is NOT a Java primitive type?", "options": ["boolean", "double", "String"],
     "difficulty": 2, "points": 1, "language": "Java", "correct_answer": "String"},
    {"question": "Which statement is used to terminate a loop in Java?", "options": ["break", "continue", "exit"],
     "difficulty": 2, "points": 1, "language": "Java", "correct_answer": "break"},

    # Java Difficulty 3 (4 Questions)
    {"question": "What is the purpose of 'super' in Java?",
     "options": ["Call parent constructor", "Exit loop", "Create object"], "difficulty": 3, "points": 3,
     "language": "Java", "correct_answer": "Call parent constructor"},
    {"question": "What data structure does Java’s HashMap use internally?", "options": ["Array", "Tree", "Hash table"],
     "difficulty": 3, "points": 3, "language": "Java", "correct_answer": "Hash table"},
    {"question": "What is the default value of a boolean in Java?", "options": ["true", "false", "null"],
     "difficulty": 3, "points": 3, "language": "Java", "correct_answer": "false"},
    {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(1)"],
     "difficulty": 3, "points": 3, "language": "Java", "correct_answer": "O(log n)"},

    # ✅ Python Questions (Added more)
    {"question": "What symbol is used for single-line comments in Python?", "options": ["//", "#", "/*"],
     "difficulty": 1, "points": 1, "language": "Python", "correct_answer": "#"},
    {"question": "Which function is used to output text in Python?", "options": ["echo", "print", "display"],
     "difficulty": 1, "points": 1, "language": "Python", "correct_answer": "print"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".python", ".pt"],
     "difficulty": 1, "points": 1, "language": "Python", "correct_answer": ".py"},

    # 🔹 Python Difficulty 2 (3 Questions)
    {"question": "Which data type is **immutable** in Python?", "options": ["List", "Dictionary", "Tuple"],
     "difficulty": 2, "points": 1, "language": "Python", "correct_answer": "Tuple"},
    {"question": "What keyword is used to define a function in Python?", "options": ["func", "define", "def"],
     "difficulty": 2, "points": 1, "language": "Python", "correct_answer": "def"},
    {"question": "How do you create a virtual environment in Python?",
     "options": ["python -m venv", "pip install venv", "virtualenv create"],
     "difficulty": 2, "points": 1, "language": "Python", "correct_answer": "python -m venv"},

    # 🔹 Python Difficulty 3 (4 Questions)
    {"question": "What is the output of `bool([])` in Python?", "options": ["True", "False", "None"],
     "difficulty": 3, "points": 3, "language": "Python", "correct_answer": "False"},
    {"question": "Which module is used for handling JSON in Python?", "options": ["json", "pickle", "dict"],
     "difficulty": 3, "points": 3, "language": "Python", "correct_answer": "json"},
    {"question": "What is the time complexity of `len()` on a Python list?", "options": ["O(1)", "O(n)", "O(log n)"],
     "difficulty": 3, "points": 3, "language": "Python", "correct_answer": "O(1)"},
    {"question": "Which of the following is NOT a valid way to declare a set in Python?",
     "options": ["set()", "{}", "[]"],
     "difficulty": 3, "points": 3, "language": "Python", "correct_answer": "[]"},

    # ✅ C++ Questions (Added more)
    {"question": "What symbol is used to end a statement in C++?", "options": [".", ";", ":"],
     "difficulty": 1, "points": 1, "language": "C++", "correct_answer": ";"},
    {"question": "Which of these is a correct way to declare an integer variable in C++?",
     "options": ["int x;", "integer x;", "var x;"],
     "difficulty": 1, "points": 1, "language": "C++", "correct_answer": "int x;"},
    {"question": "Which library is required to use `cout` in C++?", "options": ["iostream", "stdio.h", "string"],
     "difficulty": 1, "points": 1, "language": "C++", "correct_answer": "iostream"},

    # 🔹 C++ Difficulty 2 (3 Questions)
    {"question": "Which loop is guaranteed to execute at least once?", "options": ["for", "while", "do-while"],
     "difficulty": 2, "points": 1, "language": "C++", "correct_answer": "do-while"},
    {"question": "What keyword is used to define a constant in C++?", "options": ["final", "const", "static"],
     "difficulty": 2, "points": 1, "language": "C++", "correct_answer": "const"},
    {"question": "Which operator is used to allocate memory dynamically in C++?", "options": ["malloc", "alloc", "new"],
     "difficulty": 2, "points": 1, "language": "C++", "correct_answer": "new"},

    # 🔹 C++ Difficulty 3 (4 Questions)
    {"question": "Which of the following is a correct syntax for a class in C++?",
     "options": ["class MyClass {}", "MyClass class {}", "define MyClass {}"],
     "difficulty": 3, "points": 3, "language": "C++", "correct_answer": "class MyClass {}"},
    {"question": "What is the output of `sizeof(int)` typically in a 64-bit system?", "options": ["2", "4", "8"],
     "difficulty": 3, "points": 3, "language": "C++", "correct_answer": "4"},
    {"question": "Which of the following is NOT a valid access specifier in C++?",
     "options": ["private", "protected", "hidden"],
     "difficulty": 3, "points": 3, "language": "C++", "correct_answer": "hidden"},
    {"question": "Which STL container is used to store key-value pairs?", "options": ["vector", "map", "queue"],
     "difficulty": 3, "points": 3, "language": "C++", "correct_answer": "map"}
]

@app.route("/questions", methods=["GET"])
def get_questions():
    """API endpoint to retrieve questions based on language and optional difficulty."""
    language = request.args.get("language", "").capitalize()
    difficulty = request.args.get("difficulty", type=int)  # None if not provided

    if not language:
        return jsonify({"error": "Please provide 'language' parameter."}), 400

    # Filter questions by language, and by difficulty only if it's provided
    filtered_questions = [
        q for q in question_bank if q["language"].lower() == language.lower()
        and (difficulty is None or q["difficulty"] == difficulty)
    ]

    return jsonify(filtered_questions)

if __name__ == "__main__":
    app.run(debug=True)