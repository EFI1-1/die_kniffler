from typing import List
from .player import Player
from .dice import Dice

class Game:
    dices: List[Dice] = [Dice(), Dice(), Dice(), Dice(), Dice()]
    players: List[Player] = []
    bot: Player = None

    def menu(self):
        # Anzahl an Spieler nachfragen
        print("------------KNIFFEL MENU------------")
        while True:
            user_input = input("Anzahl Spieler (1-4): ")
            try:
                number = int(user_input)
                if number == 69:
                    print("Nice. Aber nicht richtig.")
                if 1 <= number <= 4:
                    break  # Exit loop if conversion succeeds
                print("Zahl muss zwischen 1 und 4 sein.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")
        for i in range(1, number + 1):
            self.players.append(Player(f"Player {i}"))
        print("------------------------------------")

    def start(self):
        print("-------------GAME START-------------")
        for i in range(1,13):
            print(f"ROUND {i}")
            self.round()
            print("")

    def round(self):
        for player in self.players:
            self.turn(player)
            print("")

    def turn(self, player):
        # einfach ändern das alles 3 mal wiederholt wird
        throws = 1
        keeping = ""
        while throws < 3:
            dicevals = ""
            for a in self.dices:
                a.roll()
                dicevals += str(a.value)
            print(f"{player.name}'s Turn. Dices: {dicevals}")
            choice = input("Type those you want to keep: ")
            dicevals += 1
        return