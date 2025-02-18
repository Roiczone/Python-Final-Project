class User:
    def __init__(self, name):
        self.name = name
        self.history = []  # List of answered Question objects

    def record_attempt(self, question, correct):
        self.history.append((question, correct))