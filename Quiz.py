
from AdaptiveQuiz import AdaptiveQuiz

if __name__ == "__main__":
    language_choice = input("Select a programming language (Java, Python, C++): ").lower()  # ✅ Convert to lowercase
    quiz = AdaptiveQuiz(language_choice)
    quiz.start_quiz()