import pygame

class Projectile:
    def __init__(self, start_pos, target, color, speed, power):
        self.pos = pygame.math.Vector2(start_pos)
        self.target = target
        self.color = color
        self.speed = speed
        self.power = power

    def move(self):
        # Calculate direction towards the target
        target_pos = pygame.math.Vector2(self.target.rect.center)
        direction = (target_pos - self.pos).normalize()

        # Move the projectile
        self.pos += direction * self.speed

    def draw(self, screen):
        # Draw the projectile as a small circle
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), 5)  # Adjust size as needed

    def has_hit(self):
        if self.pos.distance_to(self.target.rect.center) <= 5:
            self.target.health -= self.power  # Apply damage to the enemy
            return True
        return False
