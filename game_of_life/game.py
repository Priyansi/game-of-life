#!python3
import random
import math
import pygame
import game_of_life
pygame.init()


def draw_grid(win, grid, rows, columns, square_size):
    x, y = (0, 0)
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            if grid[row][column] == '1':
                pygame.draw.rect(
                    win, (255, 255, 255), (x, y, square_size, square_size))
            x += square_size
        x = 0
        y += square_size


def draw_window(win, grid, rows, columns, square_size):
    win.fill((0, 0, 0))
    draw_grid(win, grid, rows, columns, square_size)
    pygame.display.update()


if __name__ == "__main__":
    width_window, height_window = (500, 500)
    square_size = 10
    win = pygame.display.set_mode((width_window, height_window))
    flag = True
    space_bar_pressed = True
    clock = pygame.time.Clock()
    rows, columns = (width_window//square_size, height_window//square_size)
    grid = game_of_life.create_grid(rows, columns)
    draw_window(win, grid, rows, columns, square_size)

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        pygame.time.delay(100)
        clock.tick(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            space_bar_pressed = False if space_bar_pressed else True

        if not space_bar_pressed:
            grid = game_of_life.update_grid(grid, rows, columns)
        draw_window(win, grid, rows, columns, square_size)

    pygame.quit()
