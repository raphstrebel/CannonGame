import os

import pygame

from src.constants import Color, Dimensions
from src.cannon import CannonLeft, CannonRight
from src.barrel import BarrelLeft, BarrelRight
from src.cannonball import CannonBall
from src.player import Player
from src.obstacle import Obstacle


# Initialize Pygame
# Set window position to the top of the screen (x=0, y=0)
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
pygame.init()
# screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()
Dimensions.set_dimensions(info.current_w, info.current_h)
# # dims = Dimensions(info.current_w, info.current_h)
# Dimensions.DISPLAY_WIDTH = info.current_w
# Dimensions.DISPLAY_HEIGHT = info.current_h * 0.88  # stop screen above menu bar
# Dimensions.SKY_Y = Dimensions.DISPLAY_HEIGHT * 0.6
# Dimensions.GRASS_Y = Dimensions.DISPLAY_HEIGHT - Dimensions.SKY_Y
# Dimensions.CANNON_Y = Dimensions.SKY_Y - 25
# Dimensions.BARREL_Y = Dimensions.CANNON_Y - 5
# # DISPLAY_WIDTH, DISPLAY_HEIGHT = info.current_w, info.current_h
# # SKY_Y = DISPLAY_HEIGHT * 0.6
# # GRASS_Y = DISPLAY_HEIGHT - SKY_Y
screen = pygame.display.set_mode((Dimensions.DISPLAY_WIDTH, Dimensions.DISPLAY_HEIGHT), pygame.NOFRAME)


# Create a background surface once
background = pygame.Surface((Dimensions.DISPLAY_WIDTH, Dimensions.DISPLAY_HEIGHT))
background.fill(Color.BLUE, (0, 0, Dimensions.DISPLAY_WIDTH, Dimensions.SKY_Y))  # Sky blue
background.fill(Color.GREEN, (0, Dimensions.SKY_Y, Dimensions.DISPLAY_WIDTH, Dimensions.GRASS_Y))  # Grass green

pygame.display.set_caption("Cannon Ball")

turn = 0  # player on the left starts
cannonball: CannonBall = None

barrel_left = BarrelLeft(screen)
cannon_left = CannonLeft(background, barrel_left)
barrel_right = BarrelRight(screen)
cannon_right = CannonRight(background, barrel_right)

player_0 = Player(cannon_left)
player_1 = Player(cannon_right)
active_player = player_0
sleeping_player = player_1

hill = Obstacle(background)

# Draw static elements on the background
hill.draw()
player_0.cannon.draw()
player_1.cannon.draw()

running = True
while running:

    screen.blit(background, (0, 0))  # Blit the pre-rendered background
    active_player.cannon.barrel.draw()
    sleeping_player.cannon.barrel.draw_still()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # next player can click if cannonball is out of play
            if not cannonball:
                cannonball = active_player.cannon.shoot(screen)

    if cannonball:
        # Update and draw cannonballs
        cannonball.update_pos()
        cannonball.draw()

        # Check if the cannonball hits the sleeping player's cannon or barrel
        if sleeping_player.cannon.is_in_hit_box(cannonball):
            sleeping_player.cannon.explode(cannonball)
            cannonball = None  # Remove the cannonball on hit
        # FIXME: can right player self-explode?
        # elif active_player.cannon.is_in_hit_box(cannonball):
        #     active_player.cannon.explode(cannonball)
        #     cannonball = None  # Remove the cannonball on hit

        # Remove cannonball if it goes off-screen
        if not cannonball or not cannonball.is_in_screen():
            # next player
            if turn == 0:
                turn = 1
                active_player = player_1
                sleeping_player = player_0
            elif turn == 1:
                turn = 0
                active_player = player_0
                sleeping_player = player_1
            cannonball = None

    pygame.display.flip()  # Update display

pygame.quit()
