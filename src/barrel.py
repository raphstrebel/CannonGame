import math

import pygame
from pygame import Surface

from src.constants import (
    GREY, BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_RIGHT_X, BARREL_RIGHT_Y
)

class Barrel:

    WIDTH = 50
    HEIGHT = 10

    def __init__(self, screen: Surface):
        """Start pos of barrel"""
        self.screen = screen
        self.base_x = 0
        self.base_y = 0
        self.curr_x = 0
        self.curr_y = 0

    def draw_still(self):
        """Draw the barrel at still position (as player left them)"""
        pygame.draw.line(self.screen, GREY, (self.base_x, self.base_y), (self.curr_x, self.curr_y), self.HEIGHT)

    def draw(self):
        raise NotImplementedError('Cannot call abstract class func')

    def get_angle_limit(self):
        raise NotImplementedError('Cannot call abstract class func')


class BarrelLeft(Barrel):

    BARREL_LEFT_ANGLE_TOP_LIM = 1.56
    BARREL_LEFT_ANGLE_DOWN_LIM = -1.56

    def __init__(self, screen: Surface):
        """Start pos of barrel"""
        super().__init__(screen=screen)
        angle = 0
        self.base_x: int = BARREL_LEFT_X
        self.curr_x: int = BARREL_LEFT_X + self.WIDTH * math.cos(angle)
        self.base_y: int = BARREL_LEFT_Y
        self.curr_y: int = BARREL_LEFT_Y + self.WIDTH * math.sin(angle)

    def draw(self):
        """Draw the barrel depending on the mouse position"""

        # Get mouse position and calculate barrel angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print(mouse_x, mouse_y)
        angle = math.atan2(mouse_y - self.base_y, mouse_x - self.base_x)
        angle = self.get_angle_limit(angle)

        # Calculate barrel end position
        self.curr_x = self.base_x + self.WIDTH * math.cos(angle)
        self.curr_y = self.base_y + self.WIDTH * math.sin(angle)

        # Draw barrel
        pygame.draw.line(self.screen, GREY, (self.base_x, self.base_y), (self.curr_x, self.curr_y), self.HEIGHT)

    def get_angle_limit(self, angle: float):
        """Return the corrected angle within the allowed limits"""
        angle = min(self.BARREL_LEFT_ANGLE_TOP_LIM, angle)
        angle = max(self.BARREL_LEFT_ANGLE_DOWN_LIM, angle)
        return angle


class BarrelRight(Barrel):

    def __init__(self, screen: Surface):
        """Start pos of barrel"""
        super().__init__(screen=screen)
        angle = 0
        self.WIDTH = -self.WIDTH
        self.base_x: int = BARREL_RIGHT_X
        self.curr_x: int = BARREL_RIGHT_X + self.WIDTH * math.cos(angle)
        self.base_y: int = BARREL_RIGHT_Y
        self.curr_y: int = BARREL_RIGHT_Y + self.WIDTH * math.sin(angle)

    def draw(self):
        """Draw the barrel depending on the mouse position"""

        # Get mouse position and calculate barrel angle
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.base_y, mouse_x - self.base_x)
        angle = self.get_angle_limit(angle)

        # Calculate barrel end position
        self.curr_x = self.base_x - self.WIDTH * math.cos(angle)
        self.curr_y = self.base_y - self.WIDTH * math.sin(angle)

        # Draw barrel
        pygame.draw.line(self.screen, GREY, (self.base_x, self.base_y), (self.curr_x, self.curr_y), self.HEIGHT)

    def get_angle_limit(self, angle: float):
        """Return the corrected angle within the allowed limits"""
        if -1.56 < angle < 1.56:  # range on the right for barrel pointing to the left
            angle = -1.56 if angle < 0 else 1.56
        return angle
