import pygame as pg
import game.sprites as sp
import levels as lv

pg.init()

WIDTH, HEIGHT = 1000, 1000

screen = pg.display.set_mode((WIDTH, HEIGHT))

screen.fill((255, 255, 255))

run = True

objects = {1: sp.wall, 2: sp.L1_brick, 3: sp.L2_brick, 4: sp.L3_brick}


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i, row in enumerate(lv.level9):
        for j, col in enumerate(row):
            if lv.level9[i][j]:
                temp = objects[lv.level9[i][j]](i * 50, j * 40)
                temp.draw(screen)

    pg.display.flip()
