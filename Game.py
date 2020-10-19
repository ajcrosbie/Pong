import pygame
import random
import Objects
import time
import math
import tkinter as tk
from tkinter import messagebox


def custom():
    t = False
    choice = input('would you like to change game mode, y/n? ')
    if choice == 'y':
        GameMode = input('high or normal ')
        if GameMode == 'high':
            pass
        elif GameMode == 'normal':
            pass
        else:
            while not t:
                if GameMode == 'high':
                    t = True
                elif GameMode == 'normal':
                    t = True
    else:
        GameMode = 'normal'
    t = False
    choice = 0
    choice = input('would you like to change speed, y/n? ')
    if choice == 'y':
        print('what speed? 1 to 30 is recomended')
        speed = int(input('must be integer '))
        while not t:
            if speed % 1 > 0:
                speed = int(input(
                    'what speed? must be integer '))
            else:
                t = True
    else:
        speed = 10
    t = False
    choice = 0
    choice = input('would you like to change size of paddle, y/n ')
    if choice == 'y':
        print('what size(y co-ordinate)? 1 to 400 is recomended) ')
        size = int(input(' must be an integer '))
        while not t:
            if size % 1 > 0:
                print('what size(y co-ordinate)? 1 to 400 is recomended ')
                size = int(input('must be an integer '))
            else:
                t = True
        t = False
        print('what size(x co-ordinate)? 1 to 400 is recomended ')
        size2 = int(input(' must be an integer, must be less than 500 '))
        while not t:
            if size2 % 1 > 0 or size2 > 500:
                print('what size(y co-ordinate)? 1 to 400 is recomended ')
                size2 = int(input('must be an integer and less than 500 '))
            else:
                t = True
        size3 = (size2, size)
    else:
        size3 = (30, 100)
    choice = 0
    choice = input('do you want to change ball speed? y/n ')
    if choice == 'y':
        print('what speed? 1 to 30 is recomended')
        print('must be integer and smaller than')
        ballSpeed = int(
            input('the x axis of paddle(30 if unchanged)'))
        while not t:
            if ballSpeed % 1 > 0:
                ballSpeed = int(input(
                    'what speed? must be integer '))
            else:
                t = True
    else:
        ballSpeed = 20
    return GameMode, speed, size3, ballSpeed


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
    paddle1.pos = (1000 - paddle1.size[0] - 10, height/2 - 50)
    ball.pos = (500, 250)
    ball.dir = 0
    paddle.speed = 0
    paddle1.speed = 0


def main():
    GameMode = 'normal'
    speed = 10
    size = (30, 100)
    ballSpeed = 20
    v = input('do you want to customise the game? y/n ')
    if v == 'y':
        v = custom()
        GameMode = v[0]
        speed = v[1]
        size = v[2]
        ballSpeed = v[3]

    width = 1000
    height = 500
    score1 = 0
    score2 = 0
    win = pygame.display.set_mode((width, height))
    paddle = Objects.paddle((10, height/2 - 50), 0)
    paddle1 = Objects.paddle((1000 - size[0] - 10, height/2 - 50), 1)
    ball = Objects.ball((500, 250))
    ball.dir1 = ballSpeed
    paddle.size = size
    paddle1.size = size
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(10)

        keys = pygame.key.get_pressed()
        if GameMode == 'high':
            paddle.highMove(keys, speed)
            paddle1.highMove(keys, speed)
        elif GameMode == 'normal':
            paddle.move(keys, speed)
            paddle1.move(keys, speed)
        ball.move()
        touching(ball, paddle)
        touching(ball, paddle1)
        if ball.pos[1] < 0 or ball.pos[1] > 500:
            ball.bounce(0)

        if ball.pos[0] < 0:
            score1 = score1 + 1
            print(score1, ':', score2)
            reset(paddle, paddle1, ball, height)
        elif ball.pos[0] > width:
            score2 = score2 + 1
            print(score1, ':', score2)
            reset(paddle, paddle1, ball, height)
        redrawwindow(win, paddle, paddle1, ball)


if __name__ == '__main__':
    main()
