import math
import pygame
import random

from src.constants import Color, Dimensions

class Hill:

    def __init__(self, screen):
        """Create a hill-like obstacle between two cannons."""
        self.screen = screen
        self.x_start = int(Dimensions.DISPLAY_WIDTH // 3)
        self.x_end = int(2 * Dimensions.DISPLAY_WIDTH // 3)
        self.points = self.generate_hill()

    def generate_hill(self):
        """Generate a smooth hill using sine waves and randomness."""
        width = self.x_end - self.x_start
        peak_y = random.randint(Dimensions.HILL_HEIGHT_MIN, Dimensions.HILL_HEIGHT_MAX)  # Random peak height

        points = []
        for x in range(self.x_start, self.x_end+5, 5):
            norm_x = (x - self.x_start) / width * math.pi  # Normalize x to π range
            y_offset = math.sin(norm_x) * (peak_y - Dimensions.HILL_HEIGHT_MIN)  # Smooth curve
            y = Dimensions.OBSTACLE_Y - y_offset  # Place above ground
            points.append((x, int(y)))

        return points

    def draw(self):
        """Draw the hill on the screen."""
        pygame.draw.polygon(self.screen, Color.GREEN,
                            self.points + [(self.x_end, Dimensions.DISPLAY_HEIGHT),
                                           (self.x_start, Dimensions.DISPLAY_HEIGHT)], 0)
