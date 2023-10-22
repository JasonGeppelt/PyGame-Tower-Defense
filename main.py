import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CELL_SIZE, GRID_COLUMNS, GRID_ROWS, colors
from level import level_enemy_lists, level_enemy_instructions
from draw import draw_grid, draw_towers, draw_enemies, draw_ui

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Tower Defense")

clock = pygame.time.Clock()

# ------------------------------------------------
# INITIALIZE GAME ELEMENTS
# ------------------------------------------------
current_level = 2 # For now, use this to change the level!!!

# Grid elements
grid_start_x, grid_start_y = ((SCREEN_WIDTH // 2) - (GRID_COLUMNS // 2) * CELL_SIZE), 0
grid = [[None for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]

# Enemy elements
enemy_list = level_enemy_lists.get(current_level, [])
enemy_instructions = level_enemy_instructions.get(current_level, [])
active_enemy_list = [] 
time_since_last_enemy = pygame.time.get_ticks()

# UI elements
font = pygame.font.Font(None, 30) # i tried to move this to settings.py, but it wouldnt work
exit_button = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 40)
# ------------------------------------------------

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         mouse_x, mouse_y = pygame.mouse.get_pos()
        #         handle_mouse_click(mouse_x, mouse_y)
    
    # --------------------------------------------
    # DRAW
    # --------------------------------------------
    screen.fill(colors['black'])

    draw_grid(current_level, grid_start_x, grid_start_y, screen)
    draw_towers(screen)
    time_since_last_enemy = draw_enemies(time_since_last_enemy, enemy_list, grid_start_x, 
                                         grid_start_y, enemy_instructions, active_enemy_list, screen)
    draw_ui(screen, exit_button, SCREEN_WIDTH, font)
    # --------------------------------------------

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()