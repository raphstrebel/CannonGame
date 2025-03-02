import math

import pygame
from pygame import Surface

from src.constants import Color, Dimensions


class CannonBall:

    BALL_RADIUS = 5
    BALL_COLOR = Color.DARK_GREY
    GRAVITY = 0.001  # Adjust for better effect
    SPEED = 1.2  # Increased speed so the ball is visible

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
        # Ignore display height since ball falls:
        # - (0,0) is the top-left corner
        # - (width, 0) is the top-right
        # - (0, height) is the bottom-left
        # - (width, height) is the bottom-right
        return (0 <= self.x <= Dimensions.DISPLAY_WIDTH) and (self.y <= Dimensions.DISPLAY_HEIGHT)

    def draw(self):
        """Draw the cannon ball on the screen"""
        pygame.draw.circle(self.screen, self.BALL_COLOR, (self.x, self.y), self.BALL_RADIUS)
