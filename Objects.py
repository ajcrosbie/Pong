import random
import pygame


class paddle():
    def __init__(self, pos, player):
        self.colour = 255, 255, 255
        self.pos = pos
        self.player = player
        self.speed = 0
        # self.size = (30, 100)

    def move(self, keys, speed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Cspeed = 0

        if keys[pygame.K_DOWN] and self.player == 1:
            Cspeed = speed
        elif keys[pygame.K_UP] and self.player == 1:
            Cspeed = -speed
        elif keys[pygame.K_s] and self.player == 0:
            Cspeed = speed
        elif keys[pygame.K_w] and self.player == 0:
            Cspeed = -speed
        self.pos = (self.pos[0], self.pos[1] + Cspeed)
        self.speed = Cspeed

    def highMove(self, keys, speed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if keys[pygame.K_DOWN] and self.player == 1:
            self.speed = speed//10 + self.speed
        elif keys[pygame.K_UP] and self.player == 1:
            self.speed = -speed//10 + self.speed
        elif keys[pygame.K_s] and self.player == 0:
            self.speed = speed//10 + self.speed
        elif keys[pygame.K_w] and self.player == 0:
            self.speed = -speed//10 + self.speed
        self.pos = (self.pos[0], self.pos[1] + self.speed)

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, ((self.pos), (self.size)))


class ball():
    def __init__(self, pos):
        self.pos = pos
        self.colour = 255, 255, 255
        self.dir = 0
        self.size = 10
        self.dir1 = 20

    def move(self):
        self.pos = (self.pos[0] + self.dir1, self.pos[1] + self.dir)

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.pos, self.size)

    def bounce(self, paddle):
        if paddle == 0:
            self.dir = self.dir * -1
        else:
            self.dir = self.dir + paddle.speed
            self.dir1 = self.dir1 * -1
