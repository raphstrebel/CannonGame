class Color:
    WHITE = (255, 255, 255)
    GREY = (100, 100, 100)
    DARK_GREY = (60, 60, 60)
    RED = (255, 100, 0)
    BLUE = (135, 206, 250)
    GREEN = (0, 128, 0)
    BLACK = (0, 0, 0, 180)  # Black with transparency

class Direction:
    LEFT = 'left'
    RIGHT = 'right'

class Dimensions:

    def set_dimensions(width: int, height: int):
        """Set the dimensions given the screen info"""

        # Screen
        Dimensions.DISPLAY_WIDTH = int(width)
        Dimensions.DISPLAY_HEIGHT = int(height * 0.88)  # stop screen above menu bar

        # Background
        Dimensions.SKY_Y = int(Dimensions.DISPLAY_HEIGHT * 0.6)

        # Hill
        Dimensions.OBSTACLE_Y = Dimensions.SKY_Y
        Dimensions.HILL_HEIGHT_MIN = Dimensions.OBSTACLE_Y + 20
        Dimensions.HILL_HEIGHT_MAX = Dimensions.DISPLAY_HEIGHT + 100

        # Cannon
        Dimensions.CANNON_Y = Dimensions.SKY_Y - 25
        Dimensions.BARREL_Y = Dimensions.CANNON_Y - 5

        # Left Cannon
        Dimensions.CANNON_LEFT_X = 100
        Dimensions.BARREL_LEFT_X = 154

        # Right Cannon
        Dimensions.CANNON_RIGHT_X = Dimensions.DISPLAY_WIDTH - 100
        Dimensions.BARREL_RIGHT_X = Dimensions.CANNON_RIGHT_X + 5
