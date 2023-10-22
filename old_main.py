# GAME
# Manages the overall game flow, including starting and ending the game,
# and handling transitions between game states (e.g., menus, gameplay, game over).

import pygame
import sys
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE, health, money
from level import maze
from enemy import Enemy

class Game:
    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.maze = maze  # Store the maze
        self.path = [(x * 20 + 10, 10) for x in range(10)]  # Define the path for the enemy

        # Screen properties
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Tower Defense Prototype")

        # Tower and grid parameters
        self.tower_size = CELL_SIZE  # Size of each tower
        self.tower_options = [
            pygame.Rect(SCREEN_WIDTH * (1/4) - 25, SCREEN_HEIGHT - self.tower_size, self.tower_size, self.tower_size),  # Position and size of first tower option
            pygame.Rect(SCREEN_WIDTH * (2/4) - 25, SCREEN_HEIGHT - self.tower_size, self.tower_size, self.tower_size),  # Position and size of second tower option
            pygame.Rect(SCREEN_WIDTH * (3/4) - 25, SCREEN_HEIGHT - self.tower_size, self.tower_size, self.tower_size)   # Position and size of third tower option
        ]
        self.tower_colors = [Colors.RED, Colors.GREEN, Colors.BLUE]  # Colors associated with each tower option
        self.selected_tower = None  # The currently selected tower

        self.grid_rows = 10  # Number of rows in the grid
        self.grid_cols = 10  # Number of columns in the grid
        self.cell_size = self.tower_size  # Size of each cell in the grid, same as tower size

        self.start_x = (self.SCREEN_WIDTH - self.grid_cols * self.cell_size) / 2  # X-coordinate to start drawing the grid
        self.available_vertical_space = self.SCREEN_HEIGHT - self.tower_size  # Available vertical space for the grid
        self.grid_height = self.grid_rows * self.cell_size  # Height of the grid
        self.start_y = (self.available_vertical_space - self.grid_height) / 2  # Y-coordinate to start drawing the grid

        # Initialize grid
        self.grid = [[pygame.Rect(self.start_x + x * self.cell_size, self.start_y + y * self.cell_size, self.cell_size, self.cell_size) for x in range(self.grid_cols)] for y in range(self.grid_rows)]
        self.grid_colors = [[Colors.WHITE for _ in range(self.grid_cols)] for _ in range(self.grid_rows)]

        # Initialize game variables
        self.health = health
        self.money = money

        # Initialize enemies list
        self.enemies = []

        # Initialize exit button
        self.exit_button = pygame.Rect(self.SCREEN_WIDTH - 120, 20, 100, 40)

        # Load font and colors for UI text
        self.font = pygame.font.Font(None, 30)  # Set font size to 30
        self.health_color = Colors.BLACK
        self.money_color = Colors.BLACK
        self.exit_button_color = Colors.RED
        self.exit_text_color = Colors.WHITE


        self.grid_colors = [[Colors.LIGHT_GREY if maze[row][col] == 1 else Colors.WHITE for col in range(self.grid_cols)] for row in range(self.grid_rows)]

        # Create an instance of the Enemy class with the predefined path
        self.enemy = Enemy(self.cell_size, self.start_x, self.start_y)


    # ---------------------
    # UI Manager
    # ---------------------
    def draw_ui(self):
        """Draws the user interface on the screen."""
        # Display health
        health_text = self.font.render("Health: {}".format(self.health), True, self.health_color)
        self.screen.blit(health_text, (20, 20))

        # Display money
        money_text = self.font.render("Money: ${}".format(self.money), True, self.money_color)
        self.screen.blit(money_text, (20, 60))

        # Draw exit button
        pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button)
        exit_text = self.font.render("Exit", True, self.exit_text_color)
        self.screen.blit(exit_text, (self.SCREEN_WIDTH - 100, 30))

        pygame.display.flip()

    # ---------------------
    # Input Manager
    # ---------------------
    def handle_mouse_click(self, mouse_x, mouse_y):
        """Handles mouse click events.

        Args:
            mouse_x (int): The x-coordinate of the mouse click.
            mouse_y (int): The y-coordinate of the mouse click.
        """        
        # Check if a tower option was clicked and update the selected color
        for i in range(3):
            if self.tower_options[i].collidepoint(mouse_x, mouse_y):
                self.selected_tower = self.tower_colors[i]
                break

        # Check if a grid cell was clicked and update its color
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                if self.grid[row][col].collidepoint(mouse_x, mouse_y):
                    if self.selected_tower and self.maze[row][col] == 1:  # Check if it's a wall cell
                        self.grid_colors[row][col] = self.selected_tower
                        self.selected_tower = None

        # Check if exit button was clicked
        if self.exit_button.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            sys.exit()

    # ---------------------
    # Game Loop
    # ---------------------
    def run(self):
        """Runs the game loop."""
        clock = pygame.time.Clock()  # Create a clock to control the frame rate
        
        # Initialize game elements
        current_level = 1
        enemy_list = level_enemy_lists.get(current_level, [])
        enemy_instructions = level_enemy_instructions.get(current_level, [])
        active_enemy_list = [] 

        time_since_last_enemy = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.handle_mouse_click(mouse_x, mouse_y)

            # Spawn a new enemy based on the spawn interval
            current_time = pygame.time.get_ticks()
            time_elapsed = current_time - time_since_last_enemy

            if time_elapsed >= 2000:
                if enemy_list:
                    enemy_class = enemy_list.pop(0)
                    new_enemy = enemy_class((WIDTH // 2) - (enemy_class.width // 2), (HEIGHT // 2) - (enemy_class.height // 2))
                    new_enemy.instructions = enemy_instructions.copy() # created a copy of list instead of sharing
                    active_enemy_list.append(new_enemy)
                    time_since_last_enemy = 0

                time_since_last_enemy = current_time

            # Move all enemies
            for enemy in self.enemies:
                enemy.move()

            self.screen.fill(Colors.WHITE)

            # Draw grid with lines
            for row in range(self.grid_rows):
                for col in range(self.grid_cols):
                    pygame.draw.rect(self.screen, self.grid_colors[row][col], self.grid[row][col], 0)
                    pygame.draw.rect(self.screen, Colors.GREY, self.grid[row][col], 1)

            # Draw tower options
            for i in range(3):
                pygame.draw.rect(self.screen, self.tower_colors[i], self.tower_options[i])

            # Draw all enemies
            for enemy in self.enemies:
                enemy.draw(self.screen)

            # Draw UI
            self.draw_ui()

            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 frames per second


if __name__ == "__main__":
    game = Game()
    game.run()