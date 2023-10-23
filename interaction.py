import pygame
import sys
from settings import CELL_SIZE, GRID_ROWS, GRID_COLUMNS
from tower import Tower1, Tower2, Tower3

def handle_mouse_click(mouse_x, mouse_y, selected_tower, grid_start_x, grid_start_y, grid, exit_button, tower1_choice, tower2_choice, tower3_choice, active_towers, player_money):
    if exit_button.collidepoint(mouse_x, mouse_y):
        pygame.quit()
        sys.exit()

    # Set selected tower if user clicks on one of the options
    if tower1_choice.collidepoint(mouse_x, mouse_y):
        selected_tower = 1
    if tower2_choice.collidepoint(mouse_x, mouse_y):
        selected_tower = 2
    if tower3_choice.collidepoint(mouse_x, mouse_y):
        selected_tower = 3
        
    # Set grid row and column based on where user clicks
    if grid_start_x <= mouse_x <= grid_start_x + GRID_ROWS * CELL_SIZE and grid_start_y <= mouse_y <= grid_start_y + GRID_COLUMNS * CELL_SIZE :
        grid_row = (mouse_y - grid_start_y) // CELL_SIZE
        grid_col = (mouse_x - grid_start_x) // CELL_SIZE

        if selected_tower is not None and grid[grid_row][grid_col] == 1:
            
            centered_x, centered_y = grid_start_x + grid_col * CELL_SIZE + CELL_SIZE // 2 - Tower1.width // 2, grid_start_y + grid_row * CELL_SIZE + CELL_SIZE // 2 - Tower1.height // 2
            
            if selected_tower == 1:
                new_tower = Tower1(centered_x, centered_y)
            elif selected_tower == 2:
                new_tower = Tower2(centered_x, centered_y)
            elif selected_tower == 3:
                new_tower = Tower3(centered_x, centered_y)

            player_money -= new_tower.cost
            active_towers.append(new_tower)

            # Update the grid to reflect the new tower placement
            grid[grid_row][grid_col] = 2

            selected_tower = None

    return selected_tower, active_towers, player_money


