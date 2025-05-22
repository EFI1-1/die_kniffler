import pygame
from typing import List
from .dice import Dice
from .player import Player
from .button import Button
from .score import Score

# INITALIZE
pygame.init()

# CONSTANTS
WIDTH = 800
HEIGHT = 800

# COLORS
GREEN = (34, 177, 76) # background
WHITE = (255, 255, 255) # dice, score, button background
BLACK = (0, 0, 0) # text etc.

# INITALIZE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # rendered das window
pygame.display.set_caption("Kniffel") # setzt den window namen auf Kniffel
font = pygame.font.SysFont(None, 30)

class Game:
    def __init__(self):
        self.players: List[Player] = [
            Player("Player 1"),
            Player("Player 2")
        ]
        self.dices: List[Dice] = [
            Dice(50, 150, (50, 50), screen),
            Dice(150, 150, (50, 50), screen),
            Dice(250, 150, (50, 50), screen),
            Dice(350, 150, (50, 50), screen),
            Dice(450, 150, (50, 50), screen)
        ]
        self.button = Button(50, 50, 200, 100,"Button",screen, font)
        self.game_over = False
        self.rolls_left = 3

    def roll_dice(self):
        if self.rolls_left > 0:
            for die in self.dices:
                die.roll()
            self.rolls_left -= 1

    def draw(self):
        screen.fill(WHITE)

        # Draw dice
        for die in self.dices:
            die.draw()

        # Draw Roll Button
        self.button.draw()

        # Display remaining rolls
        rolls_text = font.render(f"Rolls left: {self.rolls_left}", True, BLACK)
        screen.blit(rolls_text, (WIDTH - 200, 20))

        pygame.display.update()

    def check_click(self, pos):
        if self.button.is_clicked(pos):
            if self.rolls_left > 0:
                self.roll_dice()
        else:
            # Check if any dice were clicked for selection
            for die in self.dices:
                die.toggle(pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.check_click(event.pos)

    def mainloop(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for die in self.dices:
                        die.toggle(event.pos)
                self.handle_event(event)

            self.draw()
            clock.tick(30)