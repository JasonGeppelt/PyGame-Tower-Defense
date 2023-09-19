import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, BLACK, BLUE, RED
from tower import Tower
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Main game loop
def game_loop():
    running = True

    all_sprites = pygame.sprite.Group()
    towers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create towers and enemies
        if pygame.time.get_ticks() % 1000 == 0:
            tower = Tower(100, 100)
            enemy = Enemy(SCREEN_WIDTH, random.randint(50, 550))
            all_sprites.add(tower)
            all_sprites.add(enemy)
            towers.add(tower)
            enemies.add(enemy)

        # Update sprite groups
        all_sprites.update()

        # Draw everything
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
