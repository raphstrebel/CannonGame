import math
import pygame
from pygame import Surface

from src.constants import GREY

class Barrel:

    BASE_WIDTH = 60
    BASE_HEIGHT = 30

    def __init__(self, screen: Surface, x: int, y: int):
        """Start pos of barrel"""
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        # Get mouse position and calculate angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - (self.y + 15), mouse_x - (self.x + 30))

        # Cannon barrel
        # pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, 50, 15))
        pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, 50, 15))

        # Calculate barrel end position
        length = 50  # Barrel length
        barrel_x = self.x - 30 + length * math.cos(angle)
        barrel_y = self.y - 10 + length * math.sin(angle)
        # pygame.draw.rect(self.screen, GREY, (barrel_x, barrel_y, barrel_x, barrel_y))

        # Draw rotating barrel
        # if rev:
        #     # pygame.draw.line(screen, GREY, (x + 40, y - 10), (barrel_x, barrel_y), 10)
        #     pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, barrel_x, barrel_y))
        #     # pygame.draw.rect(screen, GREY, (start_x + 40, start_y - 10, 50, 15))
        # else:
        pygame.draw.line(self.screen, GREY, (self.x - 30, self.y - 10), (barrel_x, barrel_y), 10)
        # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, barrel_x, barrel_y))
        # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, 50, 15))