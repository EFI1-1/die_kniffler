import random
import pygame

class Dice:
    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.value = random.randint(1, 6)
        self.screen = screen
        self.selected = False

    def roll(self):
        if not self.selected:
            self.value = random.randint(1,6)

    def draw(self):
        # Dice background
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

        # Border: Red if selected, Black otherwise
        border_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color, self.rect, 5)

        # Dot color: Red if selected, Black otherwise
        dot_color = (255, 0, 0) if self.selected else (0, 0, 0)
        cx = self.x + self.size // 2
        cy = self.y + self.size // 2
        qx = self.size // 4
        qy = self.size // 4

        def dot(x_offset, y_offset):
            pygame.draw.circle(self.screen, dot_color, (self.x + x_offset, self.y + y_offset), 10)

        # DRAW DOTS
        num = self.value
        if num == 1:
            dot(self.size // 2, self.size // 2)
        elif num == 2:
            dot(qx, qy)
            dot(3 * qx, 3 * qy)
        elif num == 3:
            dot(qx, qy)
            dot(self.size // 2, self.size // 2)
            dot(3 * qx, 3 * qy)
        elif num == 4:
            dot(qx, qy)
            dot(3 * qx, qy)
            dot(qx, 3 * qy)
            dot(3 * qx, 3 * qy)
        elif num == 5:
            dot(qx, qy)
            dot(3 * qx, qy)
            dot(qx, 3 * qy)
            dot(3 * qx, 3 * qy)
            dot(self.size // 2, self.size // 2)
        elif num == 6:
            dot(qx, qy)
            dot(3 * qx, qy)
            dot(qx, self.size // 2)
            dot(3 * qx, self.size // 2)
            dot(qx, 3 * qy)
            dot(3 * qx, 3 * qy)

    def toggle(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected