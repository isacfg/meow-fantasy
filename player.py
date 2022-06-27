from this import d
import pygame, os
from settings import Settings

settings = Settings()
sourceFilDir = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.rect.x += self.direction.x * self.speed


        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        # self.rect.y += self.direction.y

    def update(self):
        self.get_input()
        self.apply_gravity()