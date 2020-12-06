import gfw
from pico2d import *
import gobj
from player import Player
from fairy import Fairy
import objgen
from bulletzone import Bulletzone
from background import Background,HorzScrollBackground

canvas_width = 1740
canvas_height = 942

def enter():
    gfw.world.init(['bg1', 'bulletzone', 'bullet', 'bonus', 'bg2', 'player'])
    global player,bulletzone
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    bulletzone = Bulletzone()
    gfw.world.add(gfw.layer.bulletzone, bulletzone)
    
    bg1 = Background('backgroung_1740x942.png')    
    gfw.world.add(gfw.layer.bg1, bg1)

    bg2 = HorzScrollBackground('clouds.png',15)
    bg2.set_scroll(50)
    gfw.world.add(gfw.layer.bg2, bg2)

def update():
    gfw.world.update()
    objgen.update()

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
