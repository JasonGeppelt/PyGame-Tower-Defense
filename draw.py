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

def draw_tower_choices(screen):
    tower1 = Tower1(SCREEN_WIDTH * (1/4) - Tower1.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower1.height // 2)
    tower2 = Tower2(SCREEN_WIDTH * (2/4) - Tower2.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower2.height // 2)
    tower3 = Tower3(SCREEN_WIDTH * (3/4) - Tower3.width // 2, (GRID_ROWS * CELL_SIZE + SCREEN_HEIGHT) // 2 - Tower3.height // 2)

    tower1_choice = pygame.draw.rect(screen, tower1.color, tower1.rect)
    tower2_choice = pygame.draw.rect(screen, tower2.color, tower2.rect)
    tower3_choice = pygame.draw.rect(screen, tower3.color, tower3.rect)

    return tower1_choice, tower2_choice, tower3_choice

def draw_enemies(time_since_last_enemy, enemy_list, x, y, enemy_instructions, active_enemy_list, screen):
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
    
    return time_since_last_enemy

def draw_ui(screen, exit_button, SCREEN_WIDTH, font, player_money, player_health):
    # Display health
    health_text = font.render("Health: {}".format(player_health), True, colors['green'])
    screen.blit(health_text, (20, 20))

    # Display money
    money_text = font.render("Money: ${}".format(player_money), True, colors['white'])
    screen.blit(money_text, (20, 60))

    # Draw exit button
    pygame.draw.rect(screen, colors['red'], exit_button)
    exit_text = font.render("Exit", True, colors['white'])
    screen.blit(exit_text, (SCREEN_WIDTH - 100, 30))

def draw_active_towers(active_towers, screen):
    for tower in active_towers:
        pygame.draw.rect(screen, tower.color, tower.rect)
