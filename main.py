import pygame

from src.constants import WHITE, DISPLAY_WIDTH, DISPLAY_HEIGHT, DIRECTION
from src.cannon import Cannon
from src.barrel import BarrelLeft, BarrelRight
from src.cannonball import CannonBall
from src.player import Player


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Cannon Ball")


turn = 0  # player on the left starts
cannonball: CannonBall = None

barrel_left = BarrelLeft(screen)
cannon_left = Cannon(screen, DIRECTION.LEFT, barrel_left)
barrel_right = BarrelRight(screen)
cannon_right = Cannon(screen, DIRECTION.RIGHT, barrel_right)

player_0 = Player(cannon_left)
player_1 = Player(cannon_right)
active_player = player_0
sleeping_player = player_1


running = True
while running:
    screen.fill(WHITE)  # Clear screen

    player_0.cannon.draw()
    player_1.cannon.draw()
    active_player.cannon.barrel.draw()
    sleeping_player.cannon.barrel.draw_still()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # next player can click if cannonball is out of play
            if not cannonball:
                cannonball = active_player.cannon.shoot()

    if cannonball:
        # Update and draw cannonballs
        cannonball.update_pos()
        cannonball.draw()

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

        # check if the cannonball hit the other cannon

    pygame.display.flip()  # Update display

pygame.quit()
