import pygame

from src.game import Game

game = Game()

running = True
while running:

    game.draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.player_click()

    game.update_cannonball()

    pygame.display.flip()  # Update display

pygame.quit()
