import math

import pygame
from pygame import Surface

from src.barrel import Barrel, BarrelRight, BarrelLeft
from src.cannonball import CannonBall
from src.constants import (
    DIRECTION, GREY, DARK_GREY, CANNON_LEFT_X, CANNON_RIGHT_X, CANNON_LEFT_Y, CANNON_RIGHT_Y
)

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
        # if direction == DIRECTION.RIGHT:
        #     self.x: int = CANNON_RIGHT_X
        #     self.y: int = CANNON_RIGHT_Y
        # elif direction == DIRECTION.LEFT:
        #     self.x: int = CANNON_LEFT_X
        #     self.y: int = CANNON_LEFT_Y
        # self.screen = screen
        # self.barrel = barrel
        # # Cannon area
        # self.base_rect = (max(self.x, self.BASE_WIDTH),
        #                   max(self.y, self.BASE_HEIGHT),
        #                   min(self.x, self.BASE_WIDTH),
        #                   min(self.y, self.BASE_HEIGHT))
        # # self.base_rect = (100, 400, 160, 430)
        # self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        # self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def draw_cannon_base(self):
        """Draw the base of the cannon (without barrel)"""
        # Base rectangle
        pygame.draw.rect(self.screen, GREY, self.base_rect)
        # Arc above base rectangle
        pygame.draw.ellipse(self.screen, GREY, self.ellipse_rect)
        # Wheel
        pygame.draw.circle(self.screen, DARK_GREY, self.wheel_center, self.WHEEL_RAD)

    def draw(self):
        """Draw the current cannon with barrel"""
        self.draw_cannon_base()

    def shoot(self):
        """Shoots a cannonball towards the mouse cursor with gravity."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.barrel.base_y, mouse_x - self.barrel.base_x)
        angle = self.barrel.get_angle_limit(angle)

        cannonball = CannonBall(self.screen, self.barrel.base_x, self.barrel.base_y, angle)
        return cannonball

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        raise NotImplementedError()


class CannonLeft(Cannon):

    def __init__(
        self,
        screen: Surface,
        barrel: BarrelLeft
    ):
        """Start pos of cannon base"""
        super().__init__()
        self.x: int = CANNON_LEFT_X
        self.y: int = CANNON_LEFT_Y
        self.screen = screen
        self.barrel = barrel
        # Cannon area
        self.base_rect = (max(self.x, self.BASE_WIDTH),
                          max(self.y, self.BASE_HEIGHT),
                          min(self.x, self.BASE_WIDTH),
                          min(self.y, self.BASE_HEIGHT))
        # self.base_rect = (100, 400, 160, 430)
        self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        return (self.x <= cannonball.x <= self.x + self.BASE_WIDTH and
                self.y <= cannonball.y <= self.y + self.BASE_HEIGHT)
        # return (self.x - self.BASE_WIDTH <= cannonball.x <= self.x and
        #         self.y - self.BASE_HEIGHT <= cannonball.y <= self.y)
        # return (self.base_rect[2] <= cannonball.x <= self.base_rect[0] and
        #         self.base_rect[3] <= cannonball.y <= self.base_rect[1])


class CannonRight(Cannon):

    def __init__(
        self,
        screen: Surface,
        barrel: BarrelRight
    ):
        """Start pos of cannon base"""
        super().__init__()
        self.x: int = CANNON_RIGHT_X
        self.y: int = CANNON_RIGHT_Y
        self.screen = screen
        self.barrel = barrel
        # Cannon area
        self.base_rect = (max(self.x, self.BASE_WIDTH),
                          max(self.y, self.BASE_HEIGHT),
                          min(self.x, self.BASE_WIDTH),
                          min(self.y, self.BASE_HEIGHT))
        # self.base_rect = (100, 400, 160, 430)
        self.ellipse_rect = (self.x, self.y - 15, self.BASE_WIDTH, self.BASE_HEIGHT)
        self.wheel_center =  (self.x + self.WHEEL_WIDTH, self.y + self.WHEEL_WIDTH)

    def is_in_hit_box(self, cannonball: CannonBall):
        """Return true if the cannonball position is in the cannon hit box"""
        return (self.x <= cannonball.x <= self.x + self.BASE_WIDTH and
                self.y <= cannonball.y <= self.y + self.BASE_HEIGHT)
        # return (self.x - self.BASE_WIDTH <= cannonball.x <= self.x and
        #         self.y - self.BASE_HEIGHT <= cannonball.y <= self.y)
        # return (self.base_rect[2] <= cannonball.x <= self.base_rect[0] and
        #         self.base_rect[3] <= cannonball.y <= self.base_rect[1])

