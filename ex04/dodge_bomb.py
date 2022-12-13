import pygame as pg
import random
import sys

def check_bound(obj_rct, scr_rct):

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock =pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    scrn_sfc.blit(tori_sfc, tori_rct) 

    bomb_sfc = pg.Surface((100, 100)) 
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (50, 50), 50)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    font = pg.font.SysFont("arial", 80)      #テキストのフォント設定
    text = font.render("DEATH", True, (255, 0, 0))   #テキストの文字と色の設定


    while True:
        vx *= 1.001  #爆弾を加速
        vy *= 1.001
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_dct[pg.K_w]:            #キーによる爆弾の操作
            if key_dct[pg.K_l]:
                bomb_rct.centerx -= 2
            if key_dct[pg.K_r]:
                bomb_rct.centerx += 2
        if key_dct[pg.K_g]:
            if key_dct[pg.K_u]:
                bomb_rct.centery -= 2
            if key_dct[pg.K_d]:
                bomb_rct.centery += 2
        if check_bound(tori_rct, scrn_rct) != (+1, +1):

            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        #if check_bound(bomb_rct, scrn_rct) != (+2, +2):   キー"w","g"で動かした爆弾を枠外へ出ないようにする。
        #    if key_dct[pg.K_w]:
        #        if key_dct[pg.K_l]:
        #            bomb_rct.centerx += 2
        #        if key_dct[pg.K_r]:
        #            bomb_rct.centerx -= 2
        #    if key_dct[pg.K_g]:
        #        if key_dct[pg.K_u]:
        #            bomb_rct.centery += 2
        #        if key_dct[pg.K_d]:
        #            bomb_rct.centery -= 2

        scrn_sfc.blit(tori_sfc, tori_rct) 

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        scrn_sfc.blit(text, (700, 450))   #テキストを表示

        if tori_rct.colliderect(bomb_rct):   #tori_rctとbomb_rctを逆にしてもOK
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()