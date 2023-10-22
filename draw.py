import pygame
from settings import CELL_SIZE, GRID_COLUMNS, GRID_ROWS, ENEMY_SPAWN_FREQ, health, money, colors
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
            if cell_value == 1:
                pygame.draw.rect(screen, colors['gunmetal'], rect)
            else:
                pygame.draw.rect(screen, colors['air_force_blue'], rect)

            # Draw cell borders
            pygame.draw.rect(screen, colors['khaki'], rect, 1)

def draw_towers(screen):
    tower1 = Tower1()
    tower2 = Tower2()
    tower3 = Tower3()

    pygame.draw.rect(screen, tower1.color, tower1.rect)
    pygame.draw.rect(screen, tower2.color, tower2.rect)
    pygame.draw.rect(screen, tower3.color, tower3.rect)

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

def draw_ui(screen, exit_button, SCREEN_WIDTH, font):
    # Display health
    health_text = font.render("Health: {}".format(health), True, colors['green'])
    screen.blit(health_text, (20, 20))

    # Display money
    money_text = font.render("Money: ${}".format(money), True, colors['white'])
    screen.blit(money_text, (20, 60))

    # Draw exit button
    pygame.draw.rect(screen, colors['red'], exit_button)
    exit_text = font.render("Exit", True, colors['white'])
    screen.blit(exit_text, (SCREEN_WIDTH - 100, 30))
