from .score import Score

class Player:
    def __init__(self, name):
        self.score: Score = Score()
        self.name: str = name