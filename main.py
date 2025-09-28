import pygame
import sys
from settings import *
from player import Player
from game_platform import Platform

# Initialization of Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Game")
clock = pygame.time.Clock()


# Create player and platforms
player = Player(100, 100)
platforms = [
    Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),
    Platform(300, 400, 200, 20),
    Platform(600, 300, 150, 20),
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.handle_input(platforms)

    # Draw
    screen.fill(WHITE)
    player.draw(screen)
    for platform in platforms:
        platform.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
