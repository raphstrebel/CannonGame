import math

import pygame
from pygame import Surface

from src.constants import GREY, DARK_GREY
from src.barrel import Barrel

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

    def draw_cannon_base(self):
        """Draw the base of the cannon (without barrel)"""
        # Base rectangle
        pygame.draw.rect(self.screen, 
                         GREY, 
                         (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT))
        # Arc
        # pygame.draw.arc(self.screen, GREY, (self.x, self.y - 20, 60, 40), 0, math.pi, 5)
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
        
    # def draw_barrel(self, mouse_x, mouse_y):
    #     angle = math.atan2(mouse_y - (self.y + 15), mouse_x - (self.x + 30))

    #     # Cannon barrel
    #     # pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, 50, 15))
    #     pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, 50, 15))

    #     # Calculate barrel end position
    #     length = 50  # Barrel length
    #     barrel_x = self.x - 30 + length * math.cos(angle)
    #     barrel_y = self.y - 10 + length * math.sin(angle)
    #     # pygame.draw.rect(self.screen, GREY, (barrel_x, barrel_y, barrel_x, barrel_y))

    #     # Draw rotating barrel
    #     # if rev:
    #     #     # pygame.draw.line(screen, GREY, (x + 40, y - 10), (barrel_x, barrel_y), 10)
    #     #     pygame.draw.rect(self.screen, GREY, (self.x + 40, self.y - 10, barrel_x, barrel_y))
    #     #     # pygame.draw.rect(screen, GREY, (start_x + 40, start_y - 10, 50, 15))
    #     # else:
    #     pygame.draw.line(self.screen, GREY, (self.x - 30, self.y - 10), (barrel_x, barrel_y), 10)
    #     # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, barrel_x, barrel_y))
    #     # pygame.draw.rect(self.screen, GREY, (self.x - 30, self.y - 10, 50, 15))