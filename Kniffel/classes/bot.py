from time import sleep
from typing import List
from .score import Score
from .dice import Dice

class Bot:
    dices: List[Dice] = [Dice(), Dice(), Dice(), Dice(), Dice()]

    def __init__(self):
        self.score: Score = Score()
        throws = 1
        keeping = ""
        while throws < 3:
            dicevals = ""
            for a in self.dices:
                a.roll()
                dicevals += str(a.value)
            print(f"Bot's Turn. Dices: {dicevals}")
            throws += 1
            sleep(2)

        return