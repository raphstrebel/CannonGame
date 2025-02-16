import pygame
from src.constants import (
    WHITE, DISPLAY_WIDTH, DISPLAY_HEIGHT, CANNON_LEFT_X,
    CANNON_LEFT_Y, CANNON_RIGHT_X, CANNON_RIGHT_Y,
    BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_RIGHT_X, BARREL_RIGHT_Y,
    BARREL_RIGHT_ANGLE_TOP_LIM, BARREL_RIGHT_ANGLE_DOWN_LIM,
    BARREL_LEFT_ANGLE_TOP_LIM, BARREL_LEFT_ANGLE_DOWN_LIM,
)
from src.cannon import Cannon, Barrel
from src.cannonball import CannonBall
from src.player import Player


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Cannon Ball")


turn = 0  # player on the left starts
cannonball: CannonBall = None

barrel_left = Barrel(screen, BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_LEFT_ANGLE_TOP_LIM,
                    BARREL_LEFT_ANGLE_DOWN_LIM)
cannon_left = Cannon(screen, CANNON_LEFT_X, CANNON_LEFT_Y, barrel_left)
barrel_right = Barrel(screen, BARREL_RIGHT_X, BARREL_RIGHT_Y, BARREL_RIGHT_ANGLE_TOP_LIM,
                      BARREL_RIGHT_ANGLE_DOWN_LIM)
cannon_right = Cannon(screen, CANNON_RIGHT_X, CANNON_RIGHT_Y, barrel_right)

player_0 = Player(cannon_left)
player_1 = Player(cannon_right)
curr_player = player_0

running = True
while running:
    screen.fill(WHITE)  # Clear screen

    player_0.cannon.draw()
    player_1.cannon.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # next player can click if cannonball is out of play
            if not cannonball:
                cannonball = curr_player.cannon.shoot()

    if cannonball:
        # Update and draw cannonballs
        cannonball.update_pos()
        cannonball.draw()

        # Remove cannonball if it goes off-screen
        if not cannonball.is_in_screen():
            # next player
            if turn == 0:
                turn = 1
                curr_player = player_1
            elif turn == 1:
                turn = 0
                curr_player = player_0
            cannonball = None

    pygame.display.flip()  # Update display

pygame.quit()
