import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk3_img = pg.image.load("fig/3.png")
    kk3_img = pg.transform.flip(kk3_img, True, False)
    bg2_img = pg.transform.flip(bg_img, True, False)
    kk3_rct = kk3_img.get_rect()
    kk3_rct.center = 300, 200
    tmr = 0
    move_x = 0
    move_y = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        #print(key_lst[pg.K_UP], key_lst[pg.K_DOWN], key_lst[pg.K_LEFT], key_lst[pg.K_RIGHT])
        move_x = 0
        move_y = 0
        if key_lst[pg.K_UP]:
            move_y = -1
        if key_lst[pg.K_DOWN]:
            move_y = +1
        if key_lst[pg.K_LEFT]:
            move_x = -1
        if key_lst[pg.K_RIGHT]:
            move_x = +1

        kk3_rct.move_ip(move_x -1, move_y)
        
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk3_img, kk3_rct)
        pg.display.update()
        tmr += 1   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()