import pygame
import random
import Objects
import time
import math
import tkinter as tk
from tkinter import messagebox


def redrawwindow(win, paddle, paddle1, ball):
    win.fill((0, 0, 0))
    paddle.draw(win)
    ball.draw(win)
    paddle1.draw(win)
    pygame.display.update()
    pass


def touching(ball, paddle):
    for i in range(paddle.size[1]):
        if ball.pos[1] == paddle.pos[1] + i:
            for i in range(paddle.size[0]):
                if ball.pos[0] == paddle.pos[0] + i:
                    ball.bounce(paddle)
    pass


def reset(paddle, paddle1, ball, height):
    paddle.pos = (10, height/2 - 50)
    paddle1.pos = (960, height/2 - 50)
    ball.pos = (500, 250)
    ball.dir = 0


def main():
    width = 1000
    height = 500
    score1 = 0
    score2 = 0
    win = pygame.display.set_mode((width, height))
    paddle = Objects.paddle((10, height/2 - 50), 0)
    paddle1 = Objects.paddle((960, height/2 - 50), 1)
    ball = Objects.ball((500, 250))
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(10)

        keys = pygame.key.get_pressed()
        paddle.move(keys)
        paddle1.move(keys)
        ball.move()
        touching(ball, paddle)
        touching(ball, paddle1)
        if ball.pos[1] < 0 or ball.pos[1] > 500:
            ball.bounce(0)

        if ball.pos[0] < 0:
            score1 = score1 + 1
            print(score2, ':', score1)
            reset(paddle, paddle1, ball, height)
        elif ball.pos[0] > width:
            score2 = score2 + 1
            print(score2, ':', score1)
            reset(paddle, paddle1, ball, height)
        redrawwindow(win, paddle, paddle1, ball)


if __name__ == '__main__':
    main()
