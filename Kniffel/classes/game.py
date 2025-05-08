from typing import List
from .player import Player
from .dice import Dice

class Game:
    def __init__(self):
        self.players: List[Player] = [Player("Jean"), Player("John")] # if only one player then use ai
        self.dices: List[Dice] = [Dice(), Dice(), Dice(), Dice(), Dice()]

    def start(self):
        # Theres Like 12 Rounds in one Game for each of the player.scores properties therse one round
        for i in range(0,12,1):
            self.newround()

    def newround(self):
        if len(self.players) > 1:
            # multiplayer mode
            for i in self.players:
                self.newturn(i)
            return
        else:
            return

    def newturn(self, player):
        print(f"It is your Turn {player.name}")
        rollcount = 1
        txt = "Your Dices rolled: "
        for a in self.dices:
            a.roll()
            txt += str(a.value)
        print(txt)
        while rollcount < 3:
            choice = input("Do you want to Reroll all of them? (y/n)")
            if choice == "y":
                txt = "Your Dices rolled: "
                for a in self.dices:
                    a.roll()
                    txt += str(a.value)
                print(txt)
            elif choice == "n":
                return
            rollcount += 1
        return