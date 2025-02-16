import math

import pygame
from pygame import Surface

from src.constants import DARK_GREY, DISPLAY_WIDTH, DISPLAY_HEIGHT


class CannonBall:

    BALL_RADIUS = 5
    BALL_COLOR = DARK_GREY
    GRAVITY = 0.001  # Adjust for better effect
    SPEED = 1  # Increased speed so the ball is visible


    def __init__(
        self,
        screen: Surface,
        x: int,
        y: int,
        angle: float
    ):
        """Initialize a new cannon ball"""
        self.x = x
        self.y = y
        self.vx = self.SPEED * math.cos(angle)  # Horizontal velocity
        self.vy = self.SPEED * math.sin(angle)  # Vertical velocity
        self.screen = screen

    def update_pos(self):
        """Update the position of the cannon ball"""
        self.x += self.vx  # Keep as float for smoother movement
        self.y += self.vy
        self.vy += self.GRAVITY  # Gravity affects vertical speed

    def is_in_screen(self):
        """Check if the ball is within the screen boundaries"""
        return 0 <= self.x <= DISPLAY_WIDTH and 0 <= self.y <= DISPLAY_HEIGHT

    def draw(self):
        """Draw the cannon ball on the screen"""
        pygame.draw.circle(self.screen, self.BALL_COLOR, (int(self.x), int(self.y)), self.BALL_RADIUS)
