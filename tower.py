import pygame
from settings import colors

class Tower:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.width, self.height)

    # def attack(self, enemy):
    #     current_time = pygame.time.get_ticks()
    #     if current_time - self.last_attack_time >= 1000 / self.attack_speed:
    #         distance = pygame.math.Vector2(enemy.x - self.x, enemy.y - self.y).length()
    #         if distance <= self.attack_range:
    #             enemy.take_damage(self.damage)
    #             self.last_attack_time = current_time

class Tower1(Tower):
    width, height = 35, 35
    color = colors['yellow']
    cost = 50

class Tower2(Tower):
    width, height = 35, 35
    color = colors['dark_red']
    cost = 100

class Tower3(Tower):
    width, height = 35, 35
    color = colors['azule']
    cost = 200


