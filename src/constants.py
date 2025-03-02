class Color:
    WHITE = (255, 255, 255)
    GREY = (100, 100, 100)
    DARK_GREY = (60, 60, 60)
    RED = (255, 100, 0)
    BLUE = (135, 206, 250)
    GREEN = (0, 128, 0)

class Dimensions:
    DISPLAY_WIDTH = 0
    DISPLAY_HEIGHT = 0
    SKY_Y = 0
    GRASS_Y = 0
    CANNON_Y = 0
    BARREL_Y = 0

    def set_dimensions(width: int, height: int):
        """Set the dimensions given the screen info"""

        # Screen
        Dimensions.DISPLAY_WIDTH = width
        Dimensions.DISPLAY_HEIGHT = height * 0.88  # stop screen above menu bar

        # Background
        Dimensions.SKY_Y = Dimensions.DISPLAY_HEIGHT * 0.6
        Dimensions.GRASS_Y = Dimensions.DISPLAY_HEIGHT - Dimensions.SKY_Y

        # Cannon
        Dimensions.CANNON_Y = Dimensions.SKY_Y - 25
        Dimensions.BARREL_Y = Dimensions.CANNON_Y - 5
        Dimensions.BARELL_LENGTH = 100

        # Left Cannon
        Dimensions.CANNON_LEFT_X = 100
        Dimensions.BARREL_LEFT_X = 154

        # Right Cannon
        Dimensions.CANNON_RIGHT_X = Dimensions.DISPLAY_WIDTH - 100
        Dimensions.BARREL_RIGHT_X = Dimensions.CANNON_RIGHT_X + 5
