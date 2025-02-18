from DatabaseHandler import DatabaseHandler
from Question import Question
from Quiz import Quiz
from QuizSession import QuizSession

if __name__ == "__main__":
    questions = [
        Question("What is 2 + 2?", ["3", "4", "5"], "4", "easy"),
        Question("What is 10 * 10?", ["100", "20", "50"], "100", "medium"),
        Question("What is the square root of 144?", ["10", "12", "14"], "12", "hard")
    ]

    db = DatabaseHandler()
    user = db.load_user("Alice")
    quiz = Quiz(questions)
    session = QuizSession(user, quiz)
    session.start()

    db.save_user(user)