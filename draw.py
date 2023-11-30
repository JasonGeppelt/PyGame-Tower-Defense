import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, GRID_COLUMNS, GRID_ROWS, ENEMY_SPAWN_FREQ, colors
from level import level_maps 
from tower import Tower1, Tower2, Tower3

# Draw the grid based on the level map
def draw_grid(current_level, x, y, screen):
    for row in range(GRID_ROWS):
        for col in range(GRID_COLUMNS):
            cell_value = level_maps[current_level][row][col]
            rect = pygame.Rect(col * CELL_SIZE + x,
                                row * CELL_SIZE + y, CELL_SIZE, CELL_SIZE)
            # Draw cells
            if cell_value == 0:
                pygame.draw.rect(screen, colors['air_force_blue'], rect)
            else:
                pygame.draw.rect(screen, colors['gunmetal'], rect)

            # Draw cell borders
            pygame.draw.rect(screen, colors['khaki'], rect, 1)

def draw_tower_choices(screen, player_money, selected_tower_num=None):
    # Initialize towers in a loop
    towers = [
        Tower1(SCREEN_WIDTH * (1/4) - Tower1.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower1.height // 2),
        Tower2(SCREEN_WIDTH * (2/4) - Tower2.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower2.height // 2),
        Tower3(SCREEN_WIDTH * (3/4) - Tower3.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower3.height // 2)
    ]

    tower_choices = []

    for i, tower in enumerate(towers, start=1):
        # Draw the selected tower indicator if there is one and the player can place
        if selected_tower_num == i and player_money >= tower.cost:
            indicator_rect = pygame.Rect(
                tower.rect.x - 5, tower.rect.y - 5, 
                tower.width + 10, tower.height + 10
            )
            pygame.draw.rect(screen, colors['green'], indicator_rect, 2)

        # Draw tower choice
        tower_choice = pygame.draw.rect(screen, tower.color, tower.rect)
        tower_choices.append(tower_choice)

    return tuple(tower_choices)

def draw_enemies(time_since_last_enemy, enemy_list, x, y, enemy_instructions, active_enemy_list, screen, enemy_font):
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - time_since_last_enemy
    
    if time_elapsed >= ENEMY_SPAWN_FREQ:
        if enemy_list:
            enemy_class = enemy_list.pop(0)
            new_enemy = enemy_class(CELL_SIZE + x + (CELL_SIZE // 2) - (enemy_class.width // 2), 
                                    y + (CELL_SIZE // 2) - (enemy_class.height // 2))
            new_enemy.instructions = enemy_instructions.copy() # created a copy of list instead of sharing
            active_enemy_list.append(new_enemy)
            time_since_last_enemy = 0

        time_since_last_enemy = current_time

    for enemy in active_enemy_list:
        enemy.move()
        pygame.draw.rect(screen, enemy.color, enemy.rect)

        # Render enemy health
        health_text = enemy_font.render(str(enemy.health), True, colors['white'])
        text_rect = health_text.get_rect(center=enemy.rect.center)
        screen.blit(health_text, text_rect)
    
    return time_since_last_enemy

def draw_ui(screen, exit_button, SCREEN_WIDTH, UI_font, player_money, player_health):
    # Display health
    if player_health < 0:
        player_health = 0
    health_text = UI_font.render("Health: {}".format(player_health), True, colors['green'])
    screen.blit(health_text, (20, 20))

    # Display money
    money_text = UI_font.render("Money: ${}".format(player_money), True, colors['white'])
    screen.blit(money_text, (20, 60))

    # Draw exit button
    pygame.draw.rect(screen, colors['red'], exit_button)
    exit_text = UI_font.render("Exit", True, colors['white'])
    screen.blit(exit_text, (SCREEN_WIDTH - 100, 30))

def draw_active_towers(active_towers, screen):
    for tower in active_towers:
        tower.draw(screen)

def flash_screen_red(screen, alpha):
    flash_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    flash_surface.set_alpha(alpha)
    flash_surface.fill(colors["red"])  # Red color
    screen.blit(flash_surface, (0, 0))

def game_over(screen, font):
    game_over_text = font.render("Game Over!", True, colors['white'])
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()

    # Wait for player to acknowledge game over
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                waiting = False

