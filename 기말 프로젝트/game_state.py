import gfw
from pico2d import *
from gobj import *
import gobj
from background import Background,HorzScrollBackground

def enter():
    gfw.world.init(['bg1', 'bg2'])
    bg1 = Background('backgroung_1740x942.png')    
    gfw.world.add(gfw.layer.bg1, bg1)

    bg2 = HorzScrollBackground('clouds.png',15)
    bg2.set_scroll(50)
    gfw.world.add(gfw.layer.bg2, bg2)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
