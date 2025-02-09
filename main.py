import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cannon Drawing")

# Colors
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
DARK_GREY = (60, 60, 60)

def draw_cannon(start_x, start_y, rev=False):
    # Cannon base
    pygame.draw.rect(screen, GREY, (start_x, start_y, 60, 30))  # Base rectangle
    pygame.draw.circle(screen, DARK_GREY, (start_x + 30, start_y + 30), 20)  # Wheel
    # Cannon barrel
    if rev:
        pygame.draw.rect(screen, GREY, (start_x + 40, start_y - 10, 50, 15))
    else:
        pygame.draw.rect(screen, GREY, (start_x - 30, start_y - 10, 50, 15))

running = True
while running:
    screen.fill(WHITE)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_cannon(500, 400)  # Draw cannon at position (300,400)
    draw_cannon(200, 400, rev=True)  # Draw cannon at position (500,600)

    pygame.display.flip()  # Update display

pygame.quit()
