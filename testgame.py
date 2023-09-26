import pygame  # Import the Pygame library

import sys  # Import the sys module

pygame.init()  # Initialize Pygame

# Screen dimensions
screen_width = 800  # Set the width of the screen
screen_height = 600  # Set the height of the screen

# Colors
WHITE = (255, 255, 255)  # Define a constant color: white
RED = (255, 0, 0)  # Define a constant color: red
GREEN = (0, 255, 0)  # Define a constant color: green
BLUE = (0, 0, 255)  # Define a constant color: blue

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the game window with the specified dimensions
pygame.display.set_caption("Colorful Block Placer")  # Set the caption for the game window

# Square properties
square_size = 50  # Set the size of the squares
bottom_squares = [
    pygame.Rect(50, screen_height - square_size, square_size, square_size),  # Create a rectangle for the bottom left square
    pygame.Rect(200, screen_height - square_size, square_size, square_size),  # Create a rectangle for the bottom middle square
    pygame.Rect(350, screen_height - square_size, square_size, square_size)  # Create a rectangle for the bottom right square
]

# Colors for the bottom squares
square_colors = [RED, GREEN, BLUE]  # Store colors for the bottom squares

selected_color = None  # Initialize the selected color to None (no color selected)
square_list = []  # Initialize an empty list to store square positions (x, y) and colors

while True:  # Start an infinite loop for the game

    for event in pygame.event.get():  # Check for events (user input, etc.)
        if event.type == pygame.QUIT:  # If the event is quitting the game
            pygame.quit()  # Quit Pygame
            sys.exit()  # Exit the program

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # If the event is a left mouse button click
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the mouse position

            # Check if a bottom square was clicked
            for i, rect in enumerate(bottom_squares):
                if rect.collidepoint(mouse_x, mouse_y):  # Check if the mouse position is inside a bottom square
                    selected_color = square_colors[i]  # Update the selected color based on the clicked square

            if selected_color and mouse_y < screen_height - square_size:  # If a color is selected and the mouse is in the upper area of the screen
                square_list.append((mouse_x - square_size // 2, mouse_y - square_size // 2, selected_color))  # Add a square position and color to the list
                selected_color = None  # Reset selected color after placing a square

    # Clear the screen
    screen.fill(WHITE)  # Fill the screen with the color white

    # Draw bottom squares
    for i in range(3):  # Loop through the bottom squares
        pygame.draw.rect(screen, square_colors[i], bottom_squares[i])  # Draw each bottom square with its respective color

    # Draw placed squares
    for pos in square_list:  # Loop through the list of placed squares
        pygame.draw.rect(screen, pos[2], (pos[0], pos[1], square_size, square_size))  # Draw each placed square with its respective color and position

    # Update the screen
    pygame.display.flip()  # Update the display to show the changes
