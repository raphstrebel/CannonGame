import pygame

from src.constants import *
from src.constants import (
    WHITE, DISPLAY_WIDTH, DISPLAY_HEIGHT, CANNON_LEFT_X, 
    CANNON_LEFT_Y, CANNON_RIGHT_X, CANNON_RIGHT_Y,
    BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_RIGHT_X, BARREL_RIGHT_Y,
    BARREL_RIGHT_ANGLE_TOP_LIM, BARREL_RIGHT_ANGLE_DOWN_LIM,
    BARREL_LEFT_ANGLE_TOP_LIM, BARREL_LEFT_ANGLE_DOWN_LIM,
)
from src.cannon import Cannon, Barrel


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Cannon Ball")

running = True
while running:
    screen.fill(WHITE)  # Clear screen   

    barrel_left = Barrel(screen, BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_LEFT_ANGLE_TOP_LIM, 
                         BARREL_LEFT_ANGLE_DOWN_LIM)
    cannon_left = Cannon(screen, CANNON_LEFT_X, CANNON_LEFT_Y, barrel_left)
    barrel_right = Barrel(screen, BARREL_RIGHT_X, BARREL_RIGHT_Y, BARREL_RIGHT_ANGLE_TOP_LIM, 
                          BARREL_RIGHT_ANGLE_DOWN_LIM)
    cannon_right = Cannon(screen, CANNON_RIGHT_X, CANNON_RIGHT_Y, barrel_right)

    cannon_left.draw_cannon_base()
    cannon_right.draw_cannon_base()

    cannon_left.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # cannon_left.shoot()
            cannon_left.shoot(screen)

    for ball in cannon_left.cannonballs:
        ball.update_pos()
        ball.draw(screen)
        # Remove cannonball if it goes off-screen
        if not ball.is_in_screen():
            cannon_left.cannonballs.remove(ball)
        # ball[0][0] += ball[1][0]  # Update x position
        # ball[0][1] += ball[1][1]  # Update y position
        # ball[1][1] += ball[2]  # Apply gravity (increases downward velocity)
        # pygame.draw.circle(screen, DARK_GREY, (int(ball[0][0]), int(ball[0][1])), BALL_RADIUS)

        # Remove cannonball if it goes off-screen
        # if ball[0][0] > DISPLAY_WIDTH or ball[0][0] < 0 or ball[0][1] > DISPLAY_HEIGHT or ball[0][1] < 0:
        #     cannonballs.remove(ball)

    pygame.display.flip()  # Update display

pygame.quit()
