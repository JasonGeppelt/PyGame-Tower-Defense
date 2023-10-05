import pygame

# Initialize Pygame
pygame.init()

# Maze parameters
GRID_SIZE = 50
maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]
  # Your maze structure
path = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (9, 1)]

# Initialize the screen and clock
screen_width = len(maze[0]) * GRID_SIZE
screen_height = len(maze) * GRID_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Enemy:
    def __init__(self):
        self.path_index = 0
        self.current_position = path[0]

    def move(self):
        self.path_index += 1
        if self.path_index < len(path):
            self.current_position = path[self.path_index]

enemy = Enemy()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the enemy
    pygame.draw.circle(screen, RED, (enemy.current_position[0] * GRID_SIZE + GRID_SIZE // 2,
                                     enemy.current_position[1] * GRID_SIZE + GRID_SIZE // 2), 15)

    # Move the enemy
    enemy.move()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(2)  # Adjust this value to control the speed of the enemy

# Quit Pygame
pygame.quit()
