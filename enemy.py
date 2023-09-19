import pygame
import random
from settings import RED, SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1

    def update(self):
        # Add enemy logic here
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
