import math
import pygame
from pygame import Surface

from src.constants import (
    GREY, DIRECTION, BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_RIGHT_X, BARREL_RIGHT_Y,
    BARREL_RIGHT_ANGLE_TOP_LIM, BARREL_RIGHT_ANGLE_DOWN_LIM, BARREL_LEFT_ANGLE_TOP_LIM,
    BARREL_LEFT_ANGLE_DOWN_LIM
)

class Barrel:

    WIDTH = 50
    HEIGHT = 10

    def __init__(
        self,
        screen: Surface,
        direction: DIRECTION,
    ):
        """Start pos of barrel"""
        self.screen = screen
        self.direction = direction
        angle = 0
        if direction == DIRECTION.RIGHT:
            self.WIDTH = -self.WIDTH
            self.base_x: int = BARREL_RIGHT_X
            self.curr_x: int = BARREL_RIGHT_X + self.WIDTH * math.cos(angle)
            self.base_y: int = BARREL_RIGHT_Y
            self.curr_y: int = BARREL_RIGHT_Y + self.WIDTH * math.sin(angle)
            self.angle_top_lim: float = BARREL_RIGHT_ANGLE_TOP_LIM
            self.angle_down_lim: float = BARREL_RIGHT_ANGLE_DOWN_LIM
        elif direction == DIRECTION.LEFT:
            self.base_x: int = BARREL_LEFT_X
            self.curr_x: int = BARREL_LEFT_X + self.WIDTH * math.cos(angle)
            self.base_y: int = BARREL_LEFT_Y
            self.curr_y: int = BARREL_LEFT_Y + self.WIDTH * math.sin(angle)
            self.angle_top_lim: float = BARREL_LEFT_ANGLE_TOP_LIM
            self.angle_down_lim: float = BARREL_LEFT_ANGLE_DOWN_LIM

    def draw_still(self):
        """Draw the barrel at still position (as player left them)"""
        pygame.draw.line(self.screen, GREY, (self.base_x, self.base_y), (self.curr_x, self.curr_y), self.HEIGHT)

    def draw(self):
        """Draw the barrel depending on the mouse position"""

        # Get mouse position and calculate barrel angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.base_y, mouse_x - self.base_x)
        # print("x:", mouse_x)
        # print("y:", mouse_y)

        angle = self.get_angle_limit(angle)

        # Calculate barrel end position
        self.curr_x = self.base_x + self.WIDTH * math.cos(angle)
        self.curr_y = self.base_y + self.WIDTH * math.sin(angle)

        # Draw barrel
        pygame.draw.line(self.screen, GREY, (self.base_x, self.base_y), (self.curr_x, self.curr_y), self.HEIGHT)

    def get_angle_limit(self, angle: float):
        """Return the corrected angle within the allowed limits"""
        if self.direction == DIRECTION.LEFT:
            angle = min(self.angle_top_lim, angle)  # left barrel
            angle = max(self.angle_down_lim, angle)  # left barrel
        else:
            angle = max(self.angle_top_lim, angle)  # right barrel
            angle = min(self.angle_down_lim, angle)  # right barrel
        return angle
