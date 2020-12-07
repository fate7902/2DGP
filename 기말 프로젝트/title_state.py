import gfw
from pico2d import *
import game_state

canvas_width = 1740
canvas_height = 942

def enter():
    global image
    image = load_image('res/title.png')

    global music_title
    music_title = load_music('res/bgm_title.mp3')
    music_title.repeat_play()

def update():
    pass

def draw():
    image.draw(853, 471, canvas_width,canvas_height)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        music_title.stop()
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
