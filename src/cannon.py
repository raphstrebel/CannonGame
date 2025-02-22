import math

import pygame
from pygame import Surface

from src.barrel import Barrel
from src.cannonball import CannonBall
from src.constants import (
    DIRECTION, GREY, DARK_GREY, CANNON_LEFT_X, CANNON_RIGHT_X, CANNON_LEFT_Y, CANNON_RIGHT_Y
)

class Cannon:

    BASE_WIDTH = 60
    BASE_HEIGHT = 30
    WHEEL_RAD = 20
    WHEEL_WIDTH = 30


    def __init__(
        self,
        screen: Surface,
        direction: DIRECTION,
        barrel: Barrel
    ):
        """Start pos of cannon base"""
        if direction == DIRECTION.RIGHT:
            self.x: int = CANNON_RIGHT_X
            self.y: int = CANNON_RIGHT_Y
        elif direction == DIRECTION.LEFT:
            self.x: int = CANNON_LEFT_X
            self.y: int = CANNON_LEFT_Y
        self.screen = screen
        self.barrel = barrel
        # Cannon area
        self.base_rect = (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def draw_cannon_base(self):
        """Draw the base of the cannon (without barrel)"""
        # Base rectangle
        pygame.draw.rect(self.screen, GREY, self.base_rect)
        # Arc above base rectangle
        pygame.draw.ellipse(self.screen, GREY, self.ellipse_rect)
        # Wheel
        pygame.draw.circle(self.screen, DARK_GREY, self.wheel_center, self.WHEEL_RAD)

    def draw(self):
        """Draw the current cannon with barrel"""
        self.draw_cannon_base()

    def shoot(self):
        """Shoots a cannonball towards the mouse cursor with gravity."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.barrel.base_y, mouse_x - self.barrel.base_x)
        angle = self.barrel.get_angle_limit(angle)

        cannonball = CannonBall(self.screen, self.barrel.base_x, self.barrel.base_y, angle)
        return cannonball

    def is_in_hit_box(self, x, y):
        """Return true if the position is in the cannon hit box"""

