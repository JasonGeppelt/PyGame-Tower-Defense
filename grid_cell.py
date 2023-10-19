# GRID CELL 
# Represents a cell in the game grid, handling placement and interaction of 
# towers, enemies, or other game elements.

import pygame

class GridCell:
    def __init__(self, screen_width, screen_height, Colors):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.grid_rows = 10  # Number of rows in the grid
        self.grid_cols = 10  # Number of columns in the grid
        self.cell_size = self.tower_size  # Size of each cell in the grid, same as tower size

        self.start_x = (self.screen_width - self.grid_cols * self.cell_size) / 2  # X-coordinate to start drawing the grid
        self.available_vertical_space = self.screen_height - self.tower_size  # Available vertical space for the grid
        self.grid_height = self.grid_rows * self.cell_size  # Height of the grid
        self.start_y = (self.available_vertical_space - self.grid_height) / 2  # Y-coordinate to start drawing the grid

                # Initialize grid
        self.grid = [[pygame.Rect(self.start_x + x * self.cell_size, self.start_y + y * self.cell_size, self.cell_size, self.cell_size) for x in range(self.grid_cols)] for y in range(self.grid_rows)]
        self.grid_colors = [[Colors.WHITE for _ in range(self.grid_cols)] for _ in range(self.grid_rows)]