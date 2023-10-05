# ENEMY
# Represents individual enemy units in the game, including their properties,
# movement, health, and interactions with towers.

import pygame
import math
from level import maze, start, end

class Enemy:
    def __init__(self, cell_size, start_x, start_y):
        self.current_step = 0
        self.speed = 2
        self.cell_size = cell_size // 2

        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill((255, 0, 0))

        # Calculate the initial position based on the path
        start_x, start_y = start[1] * cell_size + start_x + 12, start[0] * cell_size + start_y + 12
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)  # Use the starting point as the initial position

        # Pathfinding variables
        self.path = []  # The calculated path
        self.calculate_path()

    def calculate_path(self):
        # Run depth-first search to find the path
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.depth_first_search(start[0], start[1], visited)

    def depth_first_search(self, x, y, visited):
        visited[x][y] = True
        self.path.append((y * self.cell_size, x * self.cell_size))  # Store the path in terms of coordinates

        if (x, y) == end:
            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y) and not visited[new_x][new_y]:
                if self.depth_first_search(new_x, new_y, visited):
                    return True

        # If no valid move is possible, backtrack by removing the last added coordinate
        self.path.pop()
        return False

    def move(self):
        if self.current_step < len(self.path) - 1:
            target_x, target_y = self.path[self.current_step + 1]

            dx = target_x - self.rect.x
            dy = target_y - self.rect.y

            # Use math.atan2 instead of pygame.math.atan2
            angle = math.atan2(dy, dx)

            # Move by the speed towards the target
            self.rect.x += self.speed * math.cos(angle)
            self.rect.y += self.speed * math.sin(angle)

            # Check if the enemy has reached the target point
            if self.rect.collidepoint(target_x, target_y):
                self.current_step += 1

    def is_valid_move(self, x, y):
        # Check if the target cell is a valid path cell (0 in the maze)
        row = y // self.cell_size
        col = x // self.cell_size

        # Ensure the row and column are within bounds
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
            return maze[row][col] == 0

        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)



