import pygame

class Button:
    def __init__(self, x, y, width, height, text, screen, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (255, 255, 255)
        self.screen = screen
        self.font = font

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0,0,0))
        self.screen.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)