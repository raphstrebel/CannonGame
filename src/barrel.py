import math
import pygame
from pygame import Surface

from src.constants import GREY

class Barrel:

    WIDTH = 50
    HEIGHT = 10

    def __init__(
        self, 
        screen: Surface, 
        x: int, 
        y: int,
        angle_top_lim: float,
        angle_down_lim: float,
    ):
        """Start pos of barrel"""
        self.x = x
        self.y = y
        self.screen = screen
        self.angle_top_lim = angle_top_lim
        self.angle_down_lim = angle_down_lim

    def draw(self):
        """Draw the barrel depending on the mouse position"""
        # Get mouse position and calculate angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.y, mouse_x - self.x)

        angle = min(self.angle_top_lim, angle)
        angle = max(self.angle_down_lim, angle)

        # Cannon barrel
        # pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, 50, 15))
        # pygame.draw.rect(self.screen, GREY, (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT))

        # Calculate barrel end position
        barrel_x = self.x + self.WIDTH * math.cos(angle)
        barrel_y = self.y + self.WIDTH * math.sin(angle)
        # pygame.draw.rect(self.screen, GREY, (barrel_x, barrel_y, barrel_x, barrel_y))

        # Draw rotating barrel
        # if rev:
        #     # pygame.draw.line(screen, GREY, (x + 40, y - 10), (barrel_x, barrel_y), 10)
        #     pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, barrel_x, barrel_y))
        #     # pygame.draw.rect(screen, GREY, (start_x + 40, start_y - 10, 50, 15))
        # else:
        pygame.draw.line(self.screen, GREY, (self.x, self.y), (barrel_x, barrel_y), self.HEIGHT)
        # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, barrel_x, barrel_y))
        # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, 50, 15))