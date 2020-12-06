import random
from pico2d import *
import gfw
from fairy import *
from player import Player

BORDER = 30
MAX_FAIRY_COUNT = 5

def init():
    global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP
    BOUNDARY_LEFT = -BORDER
    BOUNDARY_DOWN = -BORDER
    BOUNDARY_RIGHT = get_canvas_width() - BORDER
    BOUNDARY_UP = get_canvas_height() - BORDER

def get_border_coords():    
    cw, ch = get_canvas_width(), get_canvas_height()
    dx = random.random()
    if dx < 0.5: dx -= 1
    dy = random.random()
    if dy < 0.5: dy -= 1

    score = Player.player.score
    speed = 1 + score / 100
    dx *= speed
    dy *= speed

    side = random.randint(1, 4)
    if side == 1:
        x = -BORDER
        y = random.random() * ch
        if dx < 0: dx = -dx
    elif side == 2:
        x = random.random() * cw
        y = -BORDER
        if dy < 0: dy = -dy
    elif side == 3:
        x = cw + BORDER
        y = random.random() * ch
        if dx > 0: dx = -dx
    else:
        x = random.random() * cw
        y = ch + BORDER
        if dy > 0: dy = -dy
    
    return x, y, dx, dy

def generate():
    x, y, dx, dy = get_border_coords()    
    mag = random.uniform(0.5, 1.0)
    m = Missile((x, y), (dx, dy), mag)
    gfw.world.add(gfw.layer.missile, m)

def generate_bonus():
    x, y, dx, dy = get_border_coords()
    Bonus = random.choice([Bluefairy, Purplefairy])    
    m = Bonus((x, y), (dx, dy))
    gfw.world.add(gfw.layer.bonus, m)

def update():
    score = Player.player.score
    fairy_count = MAX_FAIRY_COUNT + score // 50
    if gfw.world.count_at(gfw.layer.bonus) < fairy_count:
        generate_bonus()
