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
from src.cannonball import CannonBall


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Cannon Ball")


# cannonballs = []  # List to store cannonballs

# def shoot(cannon):
#     """Shoots a cannonball towards the mouse cursor."""
#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     angle = math.atan2(mouse_y - (cannon.y + 15), mouse_x - (cannon.x + 30))
#     speed = 8
#     cannonballs.append([[cannon.x + 30, cannon.y + 15], [speed * math.cos(angle), speed * math.sin(angle)]])

cannonballs: list[CannonBall] = []  # List to store cannonballs

# def shoot(cannon):
#     """Shoots a cannonball towards the mouse cursor."""
#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     angle = math.atan2(mouse_y - (cannon.y + 15), mouse_x - (cannon.x + 30))

#     cannonballs.append(CannonBall(cannon.x + 30, cannon.y + 15, angle))


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
            cannonballs.append(cannon_left.shoot())
            # shoot(cannon_left)

    # # Update and draw cannonballs
    # for ball in cannonballs[:]:  # Iterate over a copy of the list
    #     ball.update_pos()
    #     ball.draw(screen)

    #     # Remove cannonball if it goes off-screen
    #     if not ball.is_in_screen():
    #         cannonballs.remove(ball)

    # Update and draw cannonballs
    for ball in cannonballs[:]:  # Iterate over a copy of the list
        # ball[0][0] += ball[1][0]  # Update x position
        # ball[0][1] += ball[1][1]  # Update y position
        # ball.x += ball.vx
        # ball.y += ball.vy
        # pygame.draw.circle(screen, DARK_GREY, (int(ball.x), int(ball.y)), 8)
        ball.update_pos()
        ball.draw(screen)


        # Remove cannonball if it goes off-screen
        # if ball[0][0] > DISPLAY_WIDTH or ball[0][0] < 0 or ball[0][1] > DISPLAY_HEIGHT or ball[0][1] < 0:
        #     cannonballs.remove(ball)
    # if len(cannon_left.cannonballs) > 0:
    #     cannon_left.cannonballs[0].draw(screen)
    # else:
    #     cannon_left.shoot()
    #     print('no')
    # for ball in cannon_left.cannonballs[:]:  # Iterate over a copy to avoid removal issues
    #     ball.update_pos()
    #     ball.draw(screen)

    #     # if not ball.is_in_screen():
    #     #     cannon_left.cannonballs.remove(ball)  # Safe removal

    pygame.display.flip()  # Update display

pygame.quit()
