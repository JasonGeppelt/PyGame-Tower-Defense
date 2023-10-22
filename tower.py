import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, GRID_ROWS, colors

class Tower:
    def __init__(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # def attack(self, enemy):
    #     current_time = pygame.time.get_ticks()
    #     if current_time - self.last_attack_time >= 1000 / self.attack_speed:
    #         distance = pygame.math.Vector2(enemy.x - self.x, enemy.y - self.y).length()
    #         if distance <= self.attack_range:
    #             enemy.take_damage(self.damage)
    #             self.last_attack_time = current_time

class Tower1(Tower):
    width, height = 40, 40
    x, y = SCREEN_WIDTH * (1/4) - width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - height // 2
    color = colors['yellow']

class Tower2(Tower):
    width, height = 40, 40
    x, y = SCREEN_WIDTH * (2/4) - width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - height // 2
    color = colors['dark_red']

class Tower3(Tower):
    width, height = 40, 40
    x, y = SCREEN_WIDTH * (3/4) - width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - height // 2
    color = colors['azule']

