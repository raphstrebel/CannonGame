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

        # Get mouse position and calculate barrel angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.y, mouse_x - self.x)

        angle = self.get_angle_limit(angle)

        # Calculate barrel end position
        barrel_x = self.x + self.WIDTH * math.cos(angle)
        barrel_y = self.y + self.WIDTH * math.sin(angle)

        # Draw barrel
        pygame.draw.line(self.screen, GREY, (self.x, self.y), (barrel_x, barrel_y), self.HEIGHT)

    def get_angle_limit(self, angle: float):
        """Return the corrected angle within the allowed limits"""
        angle = min(self.angle_top_lim, angle)
        angle = max(self.angle_down_lim, angle)
        return angle
