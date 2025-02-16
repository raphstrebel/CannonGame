import pygame
import math
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

cannonballs = [] # TODO: only allow one cannonball

def shoot(cannon: Cannon):
    """Shoots a cannonball towards the mouse cursor."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - (cannon.barrel.y), mouse_x - (cannon.barrel.x))
    angle = cannon.barrel.get_angle_limit(angle)
    speed = 0.3
    cannonballs.append([[cannon.barrel.x, cannon.barrel.y], [speed * math.cos(angle), speed * math.sin(angle)]])


running = True
while running:
    screen.fill(WHITE)  # Clear screen   

    barrel_left = Barrel(screen, BARREL_LEFT_X, BARREL_LEFT_Y, BARREL_LEFT_ANGLE_TOP_LIM, BARREL_LEFT_ANGLE_DOWN_LIM)
    cannon_left = Cannon(screen, CANNON_LEFT_X, CANNON_LEFT_Y, barrel_left)
    barrel_right = Barrel(screen, BARREL_RIGHT_X, BARREL_RIGHT_Y, BARREL_RIGHT_ANGLE_TOP_LIM, BARREL_RIGHT_ANGLE_DOWN_LIM)
    cannon_right = Cannon(screen, CANNON_RIGHT_X, CANNON_RIGHT_Y, barrel_right)

    cannon_left.draw_cannon_base()
    cannon_right.draw_cannon_base()

    cannon_left.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # cannon_left.shoot()
            shoot(cannon_left)

    # Update and draw cannonballs
    for ball in cannonballs[:]:  # Iterate over a copy of the list
        ball[0][0] += ball[1][0]  # Update x position
        ball[0][1] += ball[1][1]  # Update y position
        BALL_RADIUS = 5
        pygame.draw.circle(screen, DARK_GREY, (int(ball[0][0]), int(ball[0][1])), BALL_RADIUS)

        # Remove cannonball if it goes off-screen
        if ball[0][0] > DISPLAY_WIDTH or ball[0][0] < 0 or ball[0][1] > DISPLAY_HEIGHT or ball[0][1] < 0:
            cannonballs.remove(ball)

    pygame.display.flip()  # Update display

pygame.quit()
