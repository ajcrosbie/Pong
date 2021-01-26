import pygame
import random
import Objects
import time


def redrawwindow(win, paddle, paddle1, ball):
    win.fill((0, 0, 0))
    paddle.draw(win)
    paddle1.draw(win)
    ball.draw(win)
    pygame.display.update()
    pass


def winQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def touching(ball, paddle, dvd=False):
    if dvd:
        for c in range(paddle.size[1]+10):
            if ball.pos[1] == paddle.pos[1]+c:
                for i in range(paddle.size[0]+10):
                    if ball.pos[0] == paddle.pos[0] + i:
                        ball.bounce(paddle)
                    if ball.pos[0] == paddle.pos[0] - i:
                        ball.bounce(paddle)

            if ball.pos[1] == paddle.pos[1]-c:  # and paddle.side == 'bottom':
                for i in range(paddle.size[0]+10):
                    if ball.pos[0] == paddle.pos[0] + i:
                        ball.bounce(paddle)
                        if ball.pos[0] == paddle.pos[0] - i:
                            ball.bounce(paddle)

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

    score1 = 0
    score2 = 0
    win = pygame.display.set_mode((width, height))
    paddle = Objects.paddle((10, height/2 - 50), 0, size)
    paddle1 = Objects.paddle((width - size[0] - 10, height/2 - 50), 1, size)
    ball = Objects.ball((width//2, height//2))
    ball.dir1 = ballSpeed
    ball.size = ballsize
    if GameMode == 'dvd':
        f = random.randrange(10, 20)
        ball.dir = ball.dir + f
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(60)
        clock.tick(10)

        keys = pygame.key.get_pressed()
        paddle.move(keys, speed)
        paddle1.move(keys, speed)
        ball.move()
        touching(ball, paddle)
        touching(ball, paddle1)
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
        redrawwindow(win, paddle, paddle1, ball)


if __name__ == '__main__':
    main()
