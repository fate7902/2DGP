import gfw
from pico2d import *
import game_state

canvas_width = 1740
canvas_height = 920

def enter():
    global image
    image = load_image('res/purple_fairy_01_65x65.png')


def update():
    pass

def draw():
    image.draw(870, 460, canvas_width,canvas_height)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
