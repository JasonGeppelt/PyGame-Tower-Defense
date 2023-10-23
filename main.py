import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CELL_SIZE, GRID_COLUMNS, colors, STARTING_HEALTH, STARTING_MONEY
from level import level_enemy_lists, level_enemy_instructions, level_maps
from draw import draw_grid, draw_tower_choices, draw_enemies, draw_ui, draw_active_towers
from interaction import handle_mouse_click

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Tower Defense")

clock = pygame.time.Clock()

# ------------------------------------------------
# INITIALIZE GAME ELEMENTS
# ------------------------------------------------
current_level = 1 # For now, use this to change the level!!!

# Grid elements
grid_start_x, grid_start_y = ((SCREEN_WIDTH // 2) - (GRID_COLUMNS // 2) * CELL_SIZE), 0
grid = level_maps.get(current_level, [])

# Enemy elements
enemy_list = level_enemy_lists.get(current_level, [])
enemy_instructions = level_enemy_instructions.get(current_level, [])
active_enemy_list = [] 
time_since_last_enemy = pygame.time.get_ticks()

# Active tower elements
active_towers = []

# UI elements
font = pygame.font.Font(None, 30) # i tried to move this to settings.py, but it wouldnt work
exit_button = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 40)
player_health = STARTING_HEALTH
player_money = STARTING_MONEY

# Interaction elements
selected_tower = None

# --------------------------------------------
# GAME LOOP
# --------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_tower, active_towers, player_money = handle_mouse_click(mouse_x, mouse_y, selected_tower, grid_start_x, 
                                                                                grid_start_y, grid, exit_button, tower1_choice, 
                                                                                tower2_choice, tower3_choice, active_towers, player_money)
    
    screen.fill(colors['black'])

    draw_grid(current_level, grid_start_x, grid_start_y, screen)
    tower1_choice, tower2_choice, tower3_choice = draw_tower_choices(screen)
    time_since_last_enemy = draw_enemies(time_since_last_enemy, enemy_list, grid_start_x, 
                                         grid_start_y, enemy_instructions, active_enemy_list, screen)
    draw_active_towers(active_towers, screen)
    draw_ui(screen, exit_button, SCREEN_WIDTH, font, player_money, player_health)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()