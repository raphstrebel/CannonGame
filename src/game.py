import os

import pygame

from src.constants import Color, Dimensions, Direction
from src.cannon import CannonLeft, CannonRight
from src.barrel import BarrelLeft, BarrelRight
from src.cannonball import CannonBall
from src.player import Player
from src.hill import Hill


class Game:

    def __init__(self):
        """Initalize a new game"""
        # Initialize Pygame
        # Set window position to the top of the screen (x=0, y=0)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        pygame.init()
        info = pygame.display.Info()
        Dimensions.set_dimensions(info.current_w, info.current_h)
        self.screen = pygame.display.set_mode((Dimensions.DISPLAY_WIDTH, Dimensions.DISPLAY_HEIGHT),
                                              pygame.NOFRAME)

        # Create a background surface once
        self.background = pygame.Surface((Dimensions.DISPLAY_WIDTH, Dimensions.DISPLAY_HEIGHT))
        self.background.fill(Color.BLUE, (0, 0, Dimensions.DISPLAY_WIDTH, Dimensions.SKY_Y))  # Sky blue
        self.background.fill(Color.GREEN, (0, Dimensions.SKY_Y, Dimensions.DISPLAY_WIDTH,
                                           Dimensions.DISPLAY_HEIGHT))  # Grass green

        pygame.display.set_caption("Cannon Ball")

        self.turn = 0  # player on the left starts
        self.cannonball: CannonBall = None

        self.player_0 = Player(self.screen, self.background, Direction.LEFT)
        self.player_1 = Player(self.screen, self.background, Direction.RIGHT)
        self.active_player = self.player_0
        self.sleeping_player = self.player_1

        self.hill = Hill(self.background)

        # Draw static elements on the background
        self.draw_background()

    def player_click(self):
        """If cannonball is out of play, next player can click to shoot"""
        if not self.cannonball:
            self.cannonball = self.active_player.cannon.shoot(self.screen)

    def next_turn(self):
        """Switch to next player"""
        if self.turn == 0:
            self.turn = 1
            self.active_player = self.player_1
            self.sleeping_player = self.player_0
        elif self.turn == 1:
            self.turn = 0
            self.active_player = self.player_0
            self.sleeping_player = self.player_1

    def update_cannonball(self):
        """Update cannonball activity, check if player is hit"""
        if self.cannonball:
            # Update and draw cannonballs
            self.cannonball.update_pos()
            self.cannonball.draw()

            # Check if the cannonball hits the sleeping player's cannon or barrel
            if self.sleeping_player.cannon.is_in_hit_box(self.cannonball):
                self.cannonball.explode()
                self.cannonball = None  # Remove the cannonball on hit
                self.active_player.show_winner_popup(self.screen)
            elif self.hill.is_in_hit_box(self.cannonball):
                self.cannonball.explode()
                self.cannonball = None  # Remove the cannonball on hit

            # FIXME: can right player self-explode?
            # elif active_player.cannon.is_in_hit_box(cannonball):
            #     active_player.cannon.explode(cannonball)
            #     cannonball = None  # Remove the cannonball on hit

            # Remove cannonball if it goes off-screen
            if not self.cannonball or not self.cannonball.is_in_screen():
                # next player
                self.next_turn()
                self.cannonball = None

    def draw_background(self):
        """Draw static elements on the background"""
        self.hill.draw()
        self.player_0.cannon.draw()
        self.player_1.cannon.draw()

    def draw_player(self):
        """Draw player activity"""
        self.screen.blit(self.background, (0, 0))  # Blit the pre-rendered background
        self.active_player.cannon.barrel.draw()
        self.sleeping_player.cannon.barrel.draw_still()
