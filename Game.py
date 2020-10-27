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
        elif GameMode == 'dvd':
            pass
        else:
            while not t:
                if GameMode == 'high':
                    t = True
                elif GameMode == 'normal':
                    t = True

    else:
        GameMode = 'normal'
    if GameMode == 'dvd':
        speed = 10
        size3 = (30, 100)
        ballSpeed = 20
        Ballsize = 20
        obsticles = []
        size = (1000, 500)
    else:

        t = False
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
        choice = input('would you like to change ball size, y/n? ')
        if choice == 'y':
            print('what ball size? 1 to 30 is recomended')
            Ballsize = int(input('must be integer '))
            while not t:
                if speed % 1 > 0:
                    Ballsize = int(input(
                        'what size? must be integer '))
                else:
                    t = True
        else:
            Ballsize = 20
        choice = input('would you like to add obsticles, y/n? ')
        if choice == 'y':
            obsticles = []
            num = int(input('how many obsticles?'))
            for i in range(num):
                location0 = int(input('where (x co-ordinate)?'))
                location1 = int(input('where (y co-ordinate)?'))
                size0 = int(input('what size (x co-ordinate)?'))
                size1 = int(input('what size (y co-ordinate)?'))
                obsticles.append(Objects.paddle(
                    (location0, location1), 'block', (size0, size1)))
        else:
            obsticles = []
        choice = input('would you like to change display size, y/n')
        if choice == 'y':
            width = int(input('what width?'))
            height = int(input('what height?'))
            size = (width, height)
        else:
            size = (1000, 500)

    return GameMode, speed, size3, ballSpeed, Ballsize, obsticles, size


def redrawwindow(win, paddle, paddle1, ball, obsticles):
    win.fill((0, 0, 0))
    paddle.draw(win)
    paddle1.draw(win)
    ball.draw(win)
    for i in obsticles:
        i.draw(win)
    pygame.display.update()
    pass


def dvdDraw(win, ball):
    win.fill((0, 0, 0))
    ball.draw(win)
    pygame.display.update()


def winQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def touching(ball, paddle):
    for i in range(paddle.size[1]):
        if ball.pos[1] == paddle.pos[1] + i:
            for i in range(paddle.size[0]):
                if ball.pos[0] == paddle.pos[0] + i:
                    ball.bounce(paddle)
    pass


def reset(paddle, paddle1, ball, height, width):
    paddle.pos = (10, height/2 - 50)
    paddle1.pos = (width - paddle1.size[0] - 10, height/2 - 50)
    ball.pos = (500, 250)
    ball.dir = 0
    paddle.speed = 0
    paddle1.speed = 0


def main():
    GameMode = 'normal'
    speed = 10
    size = (30, 100)
    ballSpeed = 20
    ballsize = 10
    ballsize = 15
    width = 1000
    height = 500
    obsticles = []
    v = input('do you want to customise the game? y/n ')
    if v == 'y':
        v = custom()
        GameMode = v[0]
        speed = v[1]
        size = v[2]
        ballSpeed = v[3]
        ballsize = v[4]
        obsticles = v[5]
        width = v[6][0]
        height = v[6][1]

    score1 = 0
    score2 = 0
    win = pygame.display.set_mode((width, height))
    paddle = Objects.paddle((10, height/2 - 50), 0, size)
    paddle1 = Objects.paddle((width - size[0] - 10, height/2 - 50), 1, size)
    ball = Objects.ball((width//2, height//2))
    ball.dir1 = ballSpeed
    ball.size = ballsize
    if GameMode == 'dvd':
        f = random.randrange(30)
        ball.dir = ball.dir + f
        colours = [(255, 0, 0), (255, 255, 0), (0, 255, 0),
                   (0, 255, 255), (0, 0, 255), (255, 0, 255)]
        colour = 0
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(10)

        if GameMode == 'dvd':
            ball.move()
            winQuit()
            if ball.pos[0] - 10 < 0 and ball.pos[1] + 10 > height:
                ball.bounce(0)
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            elif ball.pos[0] + 10 > width and ball.pos[1] + 10 > height:
                ball.bounce(0)
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            elif ball.pos[0] - 10 < 0 and ball.pos[1] - 10 < 0:
                ball.bounce(0)
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            elif ball.pos[0] + 10 > width and ball.pos[1] - 10 < 0:
                ball.bounce(0)
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]

            elif ball.pos[1] < 0 or ball.pos[1] > height:
                ball.bounce(0)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            elif ball.pos[0] < 0:
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            elif ball.pos[0] > width:
                ball.bounce(1)
                colour = colour + 1
                if colour > len(colours)-1:
                    colour = 0
                ball.colour = colours[colour]
            print(colour)
            dvdDraw(win, ball)

        else:
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
            for i in obsticles:
                touching(ball, i)
            if ball.pos[1] < 0 or ball.pos[1] > height:
                ball.bounce(0)

            if ball.pos[0] < 0:
                score1 = score1 + 1
                print(score1, ':', score2)
                reset(paddle, paddle1, ball, height, width)
            elif ball.pos[0] > width:
                score2 = score2 + 1
                print(score1, ':', score2)
                reset(paddle, paddle1, ball, height, width)
            redrawwindow(win, paddle, paddle1, ball, obsticles)


if __name__ == '__main__':
    main()
