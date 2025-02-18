import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions  # List of Question objects
        self.history = []  # Stores user performance

    def get_next_question(self):
        """Selects the next question based on difficulty adaptation."""
        if not self.history:
            return random.choice(self.questions)  # Start with a random question

        # Adjust difficulty based on performance (basic example)
        correct_rate = sum(q.correct_attempts for q in self.history) / len(self.history)
        if correct_rate > 0.7:
            difficulty_level = "hard"
        elif correct_rate < 0.3:
            difficulty_level = "easy"
        else:
            difficulty_level = "medium"

        filtered_questions = [q for q in self.questions if q.difficulty == difficulty_level]
        return random.choice(filtered_questions) if filtered_questions else random.choice(self.questions)