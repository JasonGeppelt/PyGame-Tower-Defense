import pygame
from settings import FPS, colors
from projectile import Projectile

class Tower:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.cooldown_timer = 0
        self.active_projectiles = []

    def update(self):
        # Decrease the cooldown timer if it's above 0
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

    def attack_enemies(self, enemies):
        if self.cooldown_timer == 0:  # Check if the tower is ready to attack
            for enemy in enemies:
                if self.is_in_range(enemy):
                    self.fire_projectile(enemy)
                    self.cooldown_timer = self.get_cooldown()  # Reset the cooldown timer after an attack
                    break  # Break the loop if the tower has attacked

    def is_in_range(self, enemy):
        # Calculate the distance between the tower and the enemy
        distance = pygame.math.Vector2(self.rect.center).distance_to(enemy.rect.center)
        return distance <= self.range

    def fire_projectile(self, enemy):
        # Create and add a new projectile targeting the enemy
        new_projectile = Projectile(self.rect.center, enemy, self.projectile_color, self.projectile_speed, self.projectile_power)
        self.active_projectiles.append(new_projectile)

    def get_cooldown(self):
        # Cooldown time based on the tower's attack cooldown
        return int(FPS / self.cooldown)
    
    def draw_range(self, screen):
    # Create a transparent surface
        transparent_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 0))  # Fill with transparent color

        # Draw a translucent white circle on the transparent surface
        pygame.draw.circle(transparent_surface, (255, 255, 255, 20), (self.range, self.range), self.range)

        # Blit this transparent surface onto the screen at the tower's position
        screen.blit(transparent_surface, (self.rect.centerx - self.range, self.rect.centery - self.range))

    def draw(self, screen):
        # Draw the tower itself
        self.draw_range(screen)
        pygame.draw.rect(screen, self.color, self.rect)
        for projectile in self.active_projectiles[:]:  # Iterate over a copy of the list
            projectile.move()
            if projectile.has_hit():
                self.active_projectiles.remove(projectile)
            else:
                projectile.draw(screen)

class Tower1(Tower):
    width, height = 35, 35
    color = colors['yellow']
    cost = 50
    cooldown = 1
    range = 100    
    projectile_color = color
    projectile_speed = 5
    projectile_power = 6

class Tower2(Tower):
    width, height = 35, 35
    color = colors['dark_red']
    cost = 50
    cooldown = 1
    range = 150
    projectile_color = color
    projectile_speed = 10
    projectile_power = 6

class Tower3(Tower):
    width, height = 35, 35
    color = colors['azule']
    cost = 100
    cooldown = 3
    range = 75
    projectile_color = color
    projectile_speed = 2.5
    projectile_power = 6


