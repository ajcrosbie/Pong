import pygame
import random
import Objects


def redrawwindow(win):
    win.fill((0, 0, 0))


def main():
    width = 1000
    height = 500
    win = pygame.display.set_mode((height, width))
    paddle = Objects.paddle((255, 255, 255), 0, 0)


if __name__ == '__main__':
    main()
