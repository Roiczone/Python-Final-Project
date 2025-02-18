class QuizSession:
    def __init__(self, user, quiz):
        self.user = user
        self.quiz = quiz
        self.score = 0

    def start(self, num_questions=5):
        for _ in range(num_questions):
            question = self.quiz.get_next_question()
            print(question.text)
            for idx, option in enumerate(question.options, 1):
                print(f"{idx}. {option}")
            answer = input("Enter your answer: ")
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_answer}")

            self.user.record_attempt(question, question.check_answer(answer))

        print(f"Final Score: {self.score}/{num_questions}")