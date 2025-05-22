class Score:
    ones: int = 0
    twos: int = 0
    threes: int = 0
    fours: int = 0
    fives: int = 0
    sixes: int = 0
    bonus: (int, bool) = (35, False)
    threeofakind: int = 0
    fourofakind: int = 0
    chance: int = 0
    yathzee: int = 0
    total: int = 0


    #checks ones to sixes and returns the points
    def checklower(self, diceroll, number):
        digits = [int(d) for d in str(diceroll)]
        counter = 0
        for i in digits:
            if i == number:
                counter += 1
        return counter * number