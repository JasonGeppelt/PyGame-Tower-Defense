import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CELL_SIZE, GRID_COLUMNS, GRID_ROWS, colors
from level import level_enemy_lists, level_enemy_instructions, level_maps

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

clock = pygame.time.Clock()

# ------------------------------------------------
# INITIALIZE GAME ELEMENTS
# ------------------------------------------------
current_level = 2

# Grid elements
grid_start_x, grid_start_y = ((SCREEN_WIDTH // 2) - (GRID_COLUMNS // 2) * CELL_SIZE), 0
grid = [[None for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]

# Enemy elements
enemy_list = level_enemy_lists.get(current_level, [])
enemy_instructions = level_enemy_instructions.get(current_level, [])
active_enemy_list = [] 
time_since_last_enemy = pygame.time.get_ticks()
# ------------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # --------------------------------------------
    # GAME LOGIC
    # --------------------------------------------
    # Draw the grid based on the level map
    for row in range(GRID_ROWS):
        for col in range(GRID_COLUMNS):
            cell_value = level_maps[current_level][row][col]
            rect = pygame.Rect(col * CELL_SIZE + grid_start_x,
                                row * CELL_SIZE + grid_start_y, CELL_SIZE, CELL_SIZE)

            # Draw the cell and its border
            if cell_value == 1:
                # Color the cells for 1s
                pygame.draw.rect(screen, colors['gunmetal'], rect)
            else:
                # Color the cells for 0s
                pygame.draw.rect(screen, colors['air_force_blue'], rect)

            # Draw cell borders
            pygame.draw.rect(screen, colors['khaki'], rect, 1)
    
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - time_since_last_enemy

    if time_elapsed >= 2000:
        if enemy_list:
            enemy_class = enemy_list.pop(0)
            new_enemy = enemy_class(CELL_SIZE + grid_start_x + (CELL_SIZE // 2) - (enemy_class.width // 2), 
                                    grid_start_y + (CELL_SIZE // 2) - (enemy_class.height // 2))
            new_enemy.instructions = enemy_instructions.copy() # created a copy of list instead of sharing
            active_enemy_list.append(new_enemy)
            time_since_last_enemy = 0

        time_since_last_enemy = current_time

    for enemy in active_enemy_list:
        enemy.move()
        pygame.draw.rect(screen, enemy.color, enemy.rect)
    # --------------------------------------------

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()