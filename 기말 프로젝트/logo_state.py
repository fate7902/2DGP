import gfw
from pico2d import *
import title_state
from gobj import res

canvas_width = title_state.canvas_width
canvas_height = title_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2

def enter():
    global back, bg, fg, index, file
    back = gfw.image.load(res('kpu_logo_800x600.png'))
    bg = gfw.image.load(res('progress_bg.png'))
    fg = gfw.image.load(res('progress_fg.png'))
    index = 0

    global font, display
    font = gfw.font.load(res('ENCR10B.TTF'), 30)
    display = ''
    
    global frame_interval
    frame_interval = gfw.frame_interval
    gfw.frame_interval = 0

def update():
    global index, display
    image_count = len(IMAGE_FILES)
    font_count = len(FONT_PAIRS)
    if index < image_count:
        file = IMAGE_FILES[index]
        gfw.image.load(file)
        display = file
    elif index - image_count < font_count:
        file, size = FONT_PAIRS[index - image_count]
        gfw.font.load(file, size)
        display = '%s %dpt' % (file, size)
    else:
        gfw.change(title_state)
        return
    index += 1


def draw():
    back.draw_to_origin(0, 0,canvas_width,canvas_height)
    image_count = len(IMAGE_FILES)
    font_count = len(FONT_PAIRS)
    progress = index / (image_count + font_count)
    draw_progress(center_x, 300, 680, progress)

    global display
    font.draw(center_x - 300, 250, display)
    font.draw(center_x - 50, 300, '%.1f%%' % (progress * 100))

def draw_progress(x, y, width, rate):
    l = x - width // 2
    b = y - bg.h // 2
    draw_3(bg, l, b, width, 3)
    draw_3(fg, l, b, round(width * rate), 3)

def draw_3(img, l, b, width, edge):
    img.clip_draw_to_origin(0, 0, edge, img.h, l, b, edge, img.h)
    img.clip_draw_to_origin(edge, 0, img.w - 2 * edge, img.h, l+edge, b, width - 2 * edge, img.h)
    img.clip_draw_to_origin(img.w - edge, 0, edge, img.h, l+width-edge, b, edge, img.h)
    
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

    global frame_interval
    gfw.frame_interval = frame_interval

IMAGE_FILES = [
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

FONT_PAIRS = [
    ("res/ENCR10B.TTF", 10),
    ("res/ENCR10B.TTF", 20),
    ("res/ENCR10B.TTF", 30),
    ("res/ConsolaMalgun.TTF", 10),
    ("res/ConsolaMalgun.TTF", 20),
    ("res/ConsolaMalgun.TTF", 30),
]

if __name__ == '__main__':
    gfw.run_main()
