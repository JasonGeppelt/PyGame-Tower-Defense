import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CELL_SIZE, GRID_COLUMNS, STARTING_HEALTH, STARTING_MONEY, colors
from level import get_enemy_instructions, get_enemy_list, get_level_map, get_level_count
from draw import draw_grid, draw_tower_choices, draw_enemies, draw_ui, draw_active_towers, flash_screen_red, game_over
from user_interaction import handle_mouse_click
from save_manager import save_game_state, load_game_state

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Tower Defense")

clock = pygame.time.Clock()

# ------------------------------------------------
# INITIALIZE GAME ELEMENTS
# ------------------------------------------------
# Game elements
saved_state = load_game_state()
if saved_state:
    current_level = saved_state["current_level"]
    player_health = saved_state["player_health"]
    player_money = saved_state["player_money"]
    player_score = saved_state["player_score"]
else:
    current_level = 1
    player_health = STARTING_HEALTH
    player_money = STARTING_MONEY
    player_score = 0

# Grid elements
grid_start_x, grid_start_y = ((SCREEN_WIDTH // 2) - (GRID_COLUMNS // 2) * CELL_SIZE), 0
grid = get_level_map(current_level)

# Enemy elements
enemy_font = pygame.font.Font(None, 25)
enemy_list = get_enemy_list(current_level)
enemy_instructions = get_enemy_instructions(current_level)
active_enemy_list = [] 
time_since_last_enemy = pygame.time.get_ticks()

# Active tower elements
active_towers = []

# UI elements
UI_font = pygame.font.Font(None, 30)
gameover_font = pygame.font.Font(None, 70)
exit_button = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 40)

# Interaction elements
selected_tower = None

# Flag to track if enemies have been spawned
enemies_spawned = False

# --------------------------------------------
# GAME LOOP
# --------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game_state(current_level, player_health, player_money, player_score)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_tower, active_towers, player_money = handle_mouse_click(mouse_x, mouse_y, selected_tower, grid_start_x, 
                                                                                grid_start_y, grid, exit_button, tower_choices, active_towers, player_money)
    
    screen.fill(colors['black'])

    # Draw grid, tower choices, and UI
    draw_grid(current_level, grid_start_x, grid_start_y, screen)
    tower_choices = draw_tower_choices(screen, player_money, selected_tower)
    draw_ui(screen, exit_button, SCREEN_WIDTH, UI_font, player_money, player_health, player_score)

    # Check for game over condition after updating health on screen
    if player_health <= 0:
        game_over(screen, gameover_font)
        running = False

    # Update and draw enemies
    if active_enemy_list and not enemies_spawned:
        enemies_spawned = True

    time_since_last_enemy = draw_enemies(time_since_last_enemy, enemy_list, grid_start_x, 
                                         grid_start_y, enemy_instructions, active_enemy_list, screen, enemy_font)
    
    # Draw active towers
    draw_active_towers(active_towers, screen)

    # Tower-Enemy interaction logic
    for tower in active_towers:
        tower.update()
        tower.attack_enemies(active_enemy_list)

    # Check for defeated or successful enemies update the list and player health
    for enemy in active_enemy_list:
        if enemy.health <= 0 or enemy.is_done():
            if enemy.is_done():
                player_health -= enemy.health  # Reduce player health if enemy is done
                flash_screen_red(screen, 150)
            active_enemy_list.remove(enemy)

    # Check if the level is complete and advance to the next level
    if not active_enemy_list and enemies_spawned:
        current_level += 1
        if current_level > get_level_count():
            # Loop back to the first level or end the game
            current_level = 1  # Loop back to level 1
        enemy_list = get_enemy_list(current_level)
        enemy_instructions = get_enemy_instructions(current_level)
        active_enemy_list = []
        active_towers = []
        enemies_spawned = False
        player_money += 250
        player_score += 1
        save_game_state(current_level, player_health, player_money, player_score)

    # Check if player died
    if player_health <= 0:
        game_over(screen, gameover_font)
        # Reset or start a new game
        current_level = 1
        player_health = STARTING_HEALTH
        player_money = STARTING_MONEY
        save_game_state(current_level, player_health, player_money, player_score)
        running = False

    # Render updates
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
