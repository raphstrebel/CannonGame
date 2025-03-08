import pygame
from pygame import Surface

from src.constants import Color, Dimensions, Direction
from src.cannon import CannonLeft, CannonRight
from src.barrel import BarrelLeft, BarrelRight


class Player:

    def __init__(self, screen: Surface, background: Surface, dir: Direction):
        """Initalize the player"""
        self.win = False
        self.dir = dir
        if self.dir == Direction.LEFT:
            barrel_left = BarrelLeft(screen)
            self.cannon = CannonLeft(background, barrel_left)
            self.num = 0
        elif self.dir == Direction.RIGHT:
            barrel_right = BarrelRight(screen)
            self.cannon = CannonRight(background, barrel_right)
            self.num = 1
        else:
            raise ValueError(f'Direction invalid {self.dir}')

    def show_winner_popup(self, screen: Surface):
        """Displays a 'Player Wins' popup in the center of the screen."""
        font = pygame.font.Font(None, 50)  # font and size
        text = font.render(f"Player {self.num+1} Wins", True, Color.WHITE)  # White text
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
