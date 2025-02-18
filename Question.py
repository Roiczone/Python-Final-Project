class Question:
    def __init__(self, text, options, correct_answer, difficulty):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.attempts = 0
        self.correct_attempts = 0

    def check_answer(self, answer):
        self.attempts += 1
        if answer == self.correct_answer:
            self.correct_attempts += 1
            return True
        return False