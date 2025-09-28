import pygame
from settings import *


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def handle_input(self, platforms):
        # Input handling
        keys = pygame.key.get_pressed()
        self.vel_x = 0

        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_STRENGTH

        # Gravity and Collision settings
        self.vel_y += GRAVITY
        self.collision(platforms)

        # Movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def collision(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
