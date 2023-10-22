import pygame
from settings import CELL_SIZE, colors

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.instructions = []
        self.current_direction = None 
        self.distance_moved = 0
        self.target_distance = CELL_SIZE  # Set the desired distance to move

    def move(self):
        if self.instructions:
            instruction = self.instructions[0]  # Get the first instruction without removing it
            if instruction == self.current_direction:
                if self.current_direction == "r": # right
                    self.rect.x += self.speed
                elif self.current_direction == "l": # left
                    self.rect.x -= self.speed
                elif self.current_direction == "u": # up
                    self.rect.y -= self.speed
                elif self.current_direction == "d": # down
                    self.rect.y += self.speed
                self.distance_moved += self.speed

                # Check if the distance moved reaches the desired distance
                if self.distance_moved >= self.target_distance:
                    # Adjust the position to the exact target distance
                    overshoot = self.distance_moved - self.target_distance
                    if self.current_direction == "r":
                        self.rect.x -= overshoot
                    elif self.current_direction == "l":
                        self.rect.x += overshoot
                    elif self.current_direction == "u":
                        self.rect.y += overshoot
                    elif self.current_direction == "d":
                        self.rect.y -= overshoot

                    # Remove the instruction and reset distance moved
                    self.instructions.pop(0)
                    self.distance_moved = 0
            else:
                # Set the current direction and reset the distance moved
                self.current_direction = instruction
                self.distance_moved = 0
        else:
            self.current_direction = None



class BasicEnemy(Enemy):
    width, height = 30, 30
    color = colors['blue']
    health = 10
    damage = 2
    speed = 2

class AdvancedEnemy(Enemy):
    width, height = 20, 20
    color = colors['red']
    health = 20
    damage = 5
    speed = 5
