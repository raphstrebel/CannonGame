import math
import random

import pygame
from pygame import Surface

from src.constants import Color, Dimensions
from src.cannonball import CannonBall


class Hill:

    def __init__(self, background: Surface):
        """Create a hill-like obstacle between two cannons."""
        self.screen = background
        # Random hill left X and right X
        self.x_start = random.randint(Dimensions.HILL_WIDTH_MIN_LEFT, Dimensions.HILL_WIDTH_MAX_LEFT)
        self.x_end = random.randint(Dimensions.HILL_WIDTH_MIN_RIGHT, Dimensions.HILL_WIDTH_MAX_RIGHT)
        # Random peak height
        self.peak_y = random.randint(Dimensions.HILL_HEIGHT_MIN, Dimensions.HILL_HEIGHT_MAX)
        self.generate_hill()

    def generate_hill(self):
        """Generate a smooth hill using sine waves and randomness."""

        width = self.x_end - self.x_start

        points = []
        for x in range(self.x_start, self.x_end + 5, 5):
            norm_x = (x - self.x_start) / width * math.pi  # Normalize x to π range
            y_offset = math.sin(norm_x) * (self.peak_y - Dimensions.HILL_HEIGHT_MIN)  # Smooth curve
            y = Dimensions.OBSTACLE_Y - y_offset  # Place above ground
            points.append((x, int(y)))
        self.points = points

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return True if the given (x, y) position touches the hill."""
        x, y = cannonball.x, cannonball.y
        # Explode cannonball if it hits the ground as well
        if y > Dimensions.SKY_Y:
            return True
        # Sanity checks: ball must be within hill quadrant
        if not (self.x_start < x < self.x_end):
            return False
        if self.peak_y < y:
            return False
        for hill_x, hill_y in self.points:
            if abs(x - hill_x) < 5 and y >= hill_y:  # Check proximity and if below/at hill surface
                return True
        return False

    def draw(self):
        """Draw the hill on the screen."""
        pygame.draw.polygon(self.screen, Color.GREEN,
                            self.points + [(self.x_end, Dimensions.DISPLAY_HEIGHT),
                                           (self.x_start, Dimensions.DISPLAY_HEIGHT)], 0)
