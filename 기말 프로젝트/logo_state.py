import gfw
from pico2d import *
import title_state
from gobj import res

canvas_width = title_state.canvas_width
canvas_height = title_state.canvas_height

FILES = [
    "res/purple_fairy_01_65x65.png",
    "res/purple_fairy_02_65x65.png",
    "res/purple_fairy_03_65x65.png",
    "res/purple_fairy_04_65x65.png",
    "res/purple_fairy_05_65x65.png",
    "res/purple_fairy_06_65x65.png",
    "res/blue_fairy_01_82x74.png",
    "res/blue_fairy_02_74x73.png",
    "res/blue_fairy_03_73x73.png",
    "res/blue_fairy_04_73x74.png",
    "res/blue_fairy_05_82x73.png",
    "res/blue_fairy_06_73x73.png",
    "res/bullet_zone_01_109x104.png",
    "res/bullet_zone_02_109x104.png",
    "res/bullet_zone_03_110x106.png",
    "res/bullet_zone_04_111x107.png",
    "res/bullet_zone_05_111x108.png",
    "res/bullet_zone_06_111x109.png",
    "res/bullet_zone_07_112x110.png",
    "res/bullet_zone_08_111x109.png",
    "res/bullet_zone_09_111x108.png",
    "res/bullet_zone_10_111x107.png",
    "res/bullet_zone_11_110x106.png",
    "res/bullet_zone_12_109x103.png",
    "res/player_idle_01_295x359.png",
    "res/player_idle_02_295x358.png",
    "res/player_idle_03_295x358.png",
    "res/player_idle_04_294x355.png",
    "res/player_idle_05_295x361.png",
    "res/player_idle_06_288x361.png",
    "res/player_idle_07_287x362.png",
    "res/player_idle_08_293x359.png",
    "res/player_idle_09_293x361.png",
    "res/player_idle_10_294x366.png",
    "res/player_idle_11_293x363.png",
    "res/player_idle_12_293x370.png",
    "res/player_idle_13_294x372.png",
    "res/player_idle_14_295x369.png",
    "res/player_idle_15_295x353.png",
    "res/player_idle_16_294x359.png",
    "res/player_walk_01_391x359.png",
    "res/player_walk_02_371x359.png",
    "res/player_walk_03_377x358.png",
    "res/player_walk_04_354x355.png",
    "res/player_walk_05_361x361.png",
    "res/player_walk_06_367x361.png",
    "res/player_walk_07_373x362.png",
    "res/player_walk_08_376x359.png",
    "res/player_walk_09_384x361.png",
    "res/player_walk_09_384x361.png",
    "res/player_walk_10_389x366.png",
    "res/player_walk_11_379x363.png",
    "res/player_walk_12_370x370.png",
    "res/player_walk_13_367x372.png",
    "res/player_walk_14_384x369.png",
    "res/player_walk_15_386x353.png",
    "res/player_walk_16_383x358.png",    
    ]

center_x = canvas_width // 2
center_y = canvas_height // 2

def enter():
    global back, bg, fg, index
    back = gfw.image.load(res('kpu_logo_800x600.png'))
    bg = gfw.image.load(res('progress_bg.png'))
    fg = gfw.image.load(res('progress_fg.png'))
    index = 0

def update():
    global index
    if index >= len(FILES):
        gfw.change(title_state)
        return
    file = FILES[index]
    gfw.image.load(file)
    index += 1


def draw():
    back.draw_to_origin(0, 0,canvas_width,canvas_height)
    print(index, FILES[index - 1])


def handle_event(e):
    global player    
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()


def exit():
    global back, bg, fg
    gfw.image.unload(res('kpu_logo_800x600.png'))
    gfw.image.unload(res('progress_bg.png'))
    gfw.image.unload(res('progress_fg.png'))
    del back
    del bg
    del fg

if __name__ == '__main__':
    gfw.run_main()
