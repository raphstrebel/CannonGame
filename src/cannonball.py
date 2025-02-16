import math

import pygame

from src.constants import DARK_GREY, DISPLAY_WIDTH, DISPLAY_HEIGHT


class CannonBall:

    BALL_RADIUS = 5
    BALL_COLOR = DARK_GREY
    GRAVITY = 9.81
    # SPEED = 0.3
    SPEED = 0.001



    def __init__(self, x, y, angle):
        """Initialize a new cannon ball"""
        # Each cannonball stores position, velocity, and gravity effect
        self.x = x
        self.y = y
        self.angle = angle
        self.vx = self.SPEED * math.cos(angle)  # Horizontal velocity
        self.vy = self.SPEED * math.sin(angle)  # Vertical velocity

    def update_pos(self):
        """Update the position of the cannon ball"""
        # self.x += self.speed * math.cos(self.angle)  # Update x position
        # self.y += self.speed * math.sin(self.angle)  # Update y position
        # self.angle += self.GRAVITY  # Apply gravity (increases downward velocity)
        self.x += self.vx  # Update x position
        self.y += self.vy  # Update y position
        self.vy += self.GRAVITY  # Apply gravity (accelerates downward)

    def is_in_screen(self):
        """Check if the ball is within the screen boudaries"""
        return 0 <= self.x <= DISPLAY_WIDTH and 0 <= self.y <= DISPLAY_HEIGHT

    def draw(self, screen):
        """Draw the cannon ball on the screen"""
        pygame.draw.circle(screen, self.BALL_COLOR, (int(self.x), int(self.y)), self.BALL_RADIUS)
