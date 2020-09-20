import random
import pygame


class paddle():
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

    def move(self, keys):
        if keys[pygame.K_UP]:
            speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.pos)


class ball():
    def __init__(self):
        pass

    def move(self):
        pass

    def draw(self, surface):
        pass

    def bounce(self, paddle):
        pass
