# GAME
# Manages the overall game flow, such as starting the game, ending the game, 
# and handling transitions between game states (e.g., menus, gameplay, game over).

import pygame
import sys
from settings_manager import screen_height, screen_width, Colors, health, money

class Game:
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tower Defense Prototype")

        # Initialize tower properties and grid parameters
        self.tower_size = 50
        self.tower_options = [
            pygame.Rect(screen_width * (1/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size),
            pygame.Rect(screen_width * (2/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size),
            pygame.Rect(screen_width * (3/4) - 25, screen_height - self.tower_size, self.tower_size, self.tower_size)
        ]
        self.tower_colors = [Colors.RED, Colors.GREEN, Colors.BLUE]
        self.selected_tower = None

        self.grid_rows = 10
        self.grid_cols = 10
        self.cell_size = self.tower_size

        self.start_x = (self.screen_width - self.grid_cols * self.cell_size) / 2
        self.available_vertical_space = self.screen_height - self.tower_size
        self.grid_height = self.grid_rows * self.cell_size
        self.start_y = (self.available_vertical_space - self.grid_height) / 2

        if self.start_y < 0:
            self.start_y = 0
        elif self.start_y + self.grid_height > self.available_vertical_space:
            self.start_y = self.available_vertical_space - self.grid_height

        self.grid = [[pygame.Rect(self.start_x + x * self.cell_size, self.start_y + y * self.cell_size, self.cell_size, self.cell_size) for x in range(self.grid_cols)] for y in range(self.grid_rows)]
        self.grid_colors = [[Colors.WHITE for _ in range(self.grid_cols)] for _ in range(self.grid_rows)]

        # Initialize game variables
        self.health = health
        self.money = money

        # Initialize exit button
        self.exit_button = pygame.Rect(self.screen_width - 120, 20, 100, 40)

        # Load font and colors for UI text
        self.font = pygame.font.Font(None, 30)  # Set font size to 30
        self.health_color = Colors.BLACK
        self.money_color = Colors.BLACK
        self.exit_button_color = Colors.RED
        self.exit_text_color = Colors.WHITE

    def draw_ui(self):
        # Display health
        health_text = self.font.render("Health: {}".format(self.health), True, self.health_color)
        self.screen.blit(health_text, (20, 20))

        # Display money
        money_text = self.font.render("Money: ${}".format(self.money), True, self.money_color)
        self.screen.blit(money_text, (20, 60))

        # Draw exit button
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button)
        exit_text = self.font.render("Exit", True, self.exit_text_color)
        self.screen.blit(exit_text, (self.screen_width - 100, 30))

        pygame.display.flip()

    def handle_mouse_click(self, mouse_x, mouse_y):
    # Check if a tower option was clicked and update the selected color
        for i in range(3):
            if self.tower_options[i].collidepoint(mouse_x, mouse_y):
                self.selected_tower = self.tower_colors[i]
                break

        # Check if a grid cell was clicked and update its color
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                if self.grid[row][col].collidepoint(mouse_x, mouse_y):
                    if self.selected_tower:
                        self.grid_colors[row][col] = self.selected_tower
                        self.selected_tower = None  # Reset the tower option so the user must choose again

        # Check if exit button was clicked
        if self.exit_button.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            sys.exit()

    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.handle_mouse_click(mouse_x, mouse_y)

            self.screen.fill(Colors.WHITE)
            # Draw grid with lines
            for row in range(self.grid_rows):
                for col in range(self.grid_cols):
                    pygame.draw.rect(self.screen, self.grid_colors[row][col], self.grid[row][col], 0)
                    pygame.draw.rect(self.screen, Colors.BLACK, self.grid[row][col], 1)  # Draw grid cell borders in black

            # Draw tower options
            for i in range(3):
                pygame.draw.rect(self.screen, self.tower_colors[i], self.tower_options[i])

            # Draw UI
            self.draw_ui()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
