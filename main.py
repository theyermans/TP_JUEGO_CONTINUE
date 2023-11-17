import pygame as pg
from player import Jugador
from constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)


screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load("assets/set_bg_03/04/game_background_4.png")
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))

juego_ejecutandose = True
jugador = Jugador(0, 0, frame_rate=40, speed_walk=20, speed_run=40)


while juego_ejecutandose:
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
    
    
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        jugador.walk(direction='Left')
    elif keys[pg.K_RIGHT]:
        jugador.walk(direction='Right')
    else:
        jugador.stay()
    if keys[pg.K_SPACE]:
        jugador.jump()

    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    jugador.update(delta_ms)
    jugador.draw(screen)
    keys = pg.key.get_pressed()
    pg.display.update()
    

pg.quit()
    
if __name__ == '__main__':
    
    
    pass