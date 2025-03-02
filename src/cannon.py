import math
import time

import pygame
from pygame import Surface

from src.barrel import Barrel, BarrelRight, BarrelLeft
from src.cannonball import CannonBall
from src.constants import Color, Dimensions

class Cannon:

    BASE_WIDTH = 60
    BASE_HEIGHT = 30
    WHEEL_RAD = 20
    WHEEL_WIDTH = 30


    def __init__(self):
        """Start pos of cannon base"""
        self.x: int = 0
        self.y: int = 0
        self.screen: Surface = None
        self.barrel: Barrel = None
        self.base_rect: tuple = None
        self.ellipse_rect: tuple = None
        self.wheel_center: tuple = None

    def draw_cannon_base(self):
        """Draw the base of the cannon (without barrel)"""
        print(self.base_rect)
        # Base rectangle
        pygame.draw.rect(self.screen, Color.GREY, self.base_rect)
        # Arc above base rectangle
        pygame.draw.ellipse(self.screen, Color.GREY, self.ellipse_rect)
        # Wheel
        pygame.draw.circle(self.screen, Color.DARK_GREY, self.wheel_center, self.WHEEL_RAD)

    def draw(self):
        """Draw the current cannon with barrel"""
        self.draw_cannon_base()

    def shoot(self, screen: Surface):
        """Shoots a cannonball towards the mouse cursor with gravity."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.barrel.base_y, mouse_x - self.barrel.base_x)
        angle = self.barrel.get_angle_limit(angle)

        cannonball = CannonBall(screen, self.barrel.base_x, self.barrel.base_y, angle)
        return cannonball

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        raise NotImplementedError()

    def explode(self, cannonball: CannonBall):
        """Animate an explosion at the cannon's position"""
        self.exploding = True
        explosion_radius = 10
        max_radius = 50

        while explosion_radius < max_radius:
            pygame.draw.circle(cannonball.screen, Color.RED, (cannonball.x, cannonball.y), explosion_radius)
            pygame.display.flip()
            time.sleep(0.05)
            explosion_radius += 5
        self.exploding = False  # Reset state after explosion


class CannonLeft(Cannon):

    def __init__(
        self,
        screen: Surface,
        barrel: BarrelLeft
    ):
        """Start pos of cannon base"""
        super().__init__()
        self.x: int = Dimensions.CANNON_LEFT_X
        self.y: int = Dimensions.CANNON_Y
        self.screen = screen
        self.barrel = barrel
        # Cannon area
        self.base_rect = (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT)
        # self.base_rect = (100, 400, 160, 430)
        self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        return (self.x <= cannonball.x <= self.x + self.BASE_WIDTH and
                self.y <= cannonball.y <= self.y + self.BASE_HEIGHT)
        # if is_in_base:
        #     return True
        # is_in_arc = (self.x <= cannonball.x <= self.x + self.BASE_WIDTH and
        #              self.y - 15 <= cannonball.y <= self.y + self.BASE_HEIGHT)


class CannonRight(Cannon):

    def __init__(
        self,
        screen: Surface,
        barrel: BarrelRight
    ):
        """Start pos of cannon base"""
        super().__init__()
        self.x: int = Dimensions.CANNON_RIGHT_X
        self.y: int = Dimensions.CANNON_Y
        self.screen = screen
        self.barrel = barrel
        # Cannon area
        self.base_rect = (self.x, self.y, self.BASE_WIDTH, self.BASE_HEIGHT)
        # self.base_rect = (max(self.x, self.BASE_WIDTH),
        #                   max(self.y, self.BASE_HEIGHT),
        #                   min(self.x, self.BASE_WIDTH),
        #                   min(self.y, self.BASE_HEIGHT))
        # self.base_rect = (100, 400, 160, 430)
        self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        return (self.x <= cannonball.x <= self.x + self.BASE_WIDTH and
                self.y <= cannonball.y <= self.y + self.BASE_HEIGHT)
