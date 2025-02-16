import math

import pygame
from pygame import Surface

from src.constants import GREY, DARK_GREY
from src.barrel import Barrel
from src.cannonball import CannonBall

class Cannon:

    BASE_WIDTH = 60
    BASE_HEIGHT = 30
    WHEEL_RAD = 20
    WHEEL_WIDTH = 30


    def __init__(
        self, 
        screen: Surface, 
        x: int, 
        y: int, 
        barrel: Barrel
    ):
        """Start pos of cannon base"""
        self.x = x
        self.y = y
        self.screen = screen
        self.barrel = barrel
        self.cannonballs: list[CannonBall] = []

    def draw_cannon_base(self):
        """Draw the base of the cannon (without barrel)"""
        # Base rectangle
        pygame.draw.rect(self.screen, 
                         GREY, 
                         (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT))
        # Arc above base rectangle
        pygame.draw.ellipse(self.screen, GREY, (self.x, self.y - 15, 60, 30))
        # Wheel
        pygame.draw.circle(self.screen, 
                           DARK_GREY, 
                           (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH), 
                           self.WHEEL_RAD)
    
    def draw(self):
        """Draw the current cannon with barrel"""
        self.draw_cannon_base()
        self.barrel.draw()

    def shoot(self):
        """Shoots a cannonball towards the mouse cursor with gravity."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.barrel.y, mouse_x - self.barrel.x)
        angle = self.barrel.get_angle_limit(angle)

        cannonball = CannonBall(self.barrel.x, self.barrel.y, angle)
        return cannonball
        self.cannonballs.append(cannonball)
        # cannonball.draw(screen)
