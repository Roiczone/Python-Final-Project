import requests
import random

class AdaptiveQuiz:
    def __init__(self, language_choice):
        self.language_choice = language_choice.capitalize()  # Normalize input
        self.difficulty = 1  # Start at difficulty level 1
        self.score = 0  # Total score
        self.questions_per_difficulty = {1: 3, 2: 3, 3: 4}  # Number of questions per difficulty
        self.passing_criteria = {1: 2, 2: 2, 3: 3}  # Required correct answers per difficulty

    def fetch_questions(self, difficulty):
        """Fetch questions from API dynamically."""
        url = f"http://127.0.0.1:5000/questions?language={self.language_choice}&{self.difficulty}"
        try:
            response = requests.get(url)
            questions = response.json()

            # Debugging: Print API response
           # print(f"🔍 API Response for {self.language_choice}, Difficulty {difficulty}: {questions}")

            if isinstance(questions, list):
                return random.sample(questions, min(len(questions), self.questions_per_difficulty[difficulty]))
            return []
        except requests.exceptions.RequestException:
            print("⚠ Error fetching questions from the API!")
            return []

    def ask_questions_for_difficulty(self):
        """Ask all questions for the current difficulty before checking the score."""
        while True:  # Repeat this difficulty until the user passes
            questions = self.fetch_questions(self.difficulty)

            if not questions:
                print("⚠ No questions available for this difficulty.")
                return False  # Stop if no questions

            total_correct = 0  # Reset correct answers counter

            for question in questions:
                print(f"\nQuestion: {question['question']}")
                print("Options:")
                for i, option in enumerate(question["options"], 1):
                    print(f"{i}. {option}")

                try:
                    answer = int(input("Choose the correct option (1, 2, or 3): "))
                    if question["options"][answer - 1] == question["correct_answer"]:
                        print("✅ Correct!")
                        total_correct += 1
                    else:
                        print(f"❌ Wrong! The correct answer is: {question['correct_answer']}")
                except (IndexError, ValueError):
                    print("⚠ Invalid choice! No points awarded.")

            # Check if user meets the passing criteria
            required_correct = self.passing_criteria[self.difficulty]
            if total_correct >= required_correct:
                print(f"🎉 Well done! You got {total_correct} correct answers and unlocked the next difficulty!")
                self.score += total_correct  # Accumulate total score
                return True  # Move to the next difficulty
            else:
                print(f"❌ You got {total_correct} correct answers, which is not enough to proceed. Retaking this difficulty...\n")

    def start_quiz(self):
        """Start the quiz with increasing difficulty."""
        while self.difficulty <= 3:
            print(f"\n🔹 --- Difficulty {self.difficulty} --- 🔹")

            if self.ask_questions_for_difficulty():
                self.difficulty += 1  # Unlock next level

                # If user completes difficulty 3 successfully, end the quiz
                if self.difficulty == 4:
                    print("\n🏆 You completed the quiz! Congratulations! 🏆")
                    return

        print("\n🏆 Quiz Over! Your Final Score:", self.score)
