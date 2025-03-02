import pygame
from pygame import Surface

from src.cannon import Cannon
from src.constants import Color, Dimensions


class Player:

    def __init__(self, num: int, cannon: Cannon):
        """Initalize the player"""
        self.win = False
        self.cannon = cannon
        self.num = num

    def show_winner_popup(self, screen: Surface):
        """Displays a 'Player Wins' popup in the center of the screen."""
        font = pygame.font.Font(None, 50)  # font and size
        text = font.render(f"Player {self.num} Wins", True, Color.WHITE)  # White text
        text_rect = text.get_rect(center=(Dimensions.DISPLAY_WIDTH // 2,
                                          Dimensions.DISPLAY_HEIGHT // 2))

        # Semi-transparent background
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill(Color.BLACK)

        screen.blit(overlay, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.update()

        # Wait for a short time or until the user clicks
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                    waiting = False
