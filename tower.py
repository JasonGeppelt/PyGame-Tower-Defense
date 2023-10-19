# TOWER
# Represents individual towers in the game, including their properties, 
# upgrades, and behavior.

import pygame

class Tower:
    # initialize Tower
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

     # Tower and grid parameters
        self.tower_size = 50  # Size of each tower
        self.tower_options = [
            pygame.Rect(screen_width * (1/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size),  # Position and size of first tower option
            pygame.Rect(screen_width * (2/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size),  # Position and size of second tower option
            pygame.Rect(screen_width * (3/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size)   # Position and size of third tower option
        ]