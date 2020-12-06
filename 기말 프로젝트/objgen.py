import random
import math
from pico2d import *
import gfw
from fairy import *
from bullet import *
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
    pattern = Player.player.pattern
    patterncount = Player.player.patterncount
    score = Player.player.score
    speed = 1 + score / 100
    
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    if pattern == 1:
        dx = 1 * math.cos(math.pi * (patterncount * 3 / 180))
        dy = 1 * math.sin(math.pi * (patterncount * 3 / 180))
        dx *= speed
        dy *= speed
        m = Bullet((x, y), (dx, dy))
        gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(1)
    elif pattern == 2:
        dx = 1 * math.cos(math.pi * (patterncount * -3 / 180))
        dy = 1 * math.sin(math.pi * (patterncount * -3 / 180))
        dx *= speed
        dy *= speed
        m = Bullet((x, y), (dx, dy))
        gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(1)
    elif pattern == 3:
        for i in range(1,5):
            dx = 1 * math.cos(math.pi * (patterncount * 3 / (180 / i)))
            dy = 1 * math.sin(math.pi * (patterncount * 3 / (180 / i)))
            dx *= speed
            dy *= speed
            m = Bullet((x, y), (dx, dy))
            gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(4)
    elif pattern == 4:
        for i in range(1,5):
            dx = 1 * math.cos(math.pi * (patterncount * -3 / (180 / i)))
            dy = 1 * math.sin(math.pi * (patterncount * -3 / (180 / i)))
            dx *= speed
            dy *= speed
            m = Bullet((x, y), (dx, dy))
            gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(4)
    elif pattern == 5:
        for i in range(1,5):
            dx = 1 * math.cos(math.pi * ((patterncount * 3 + (90 * (i - 1))) / 180))
            dy = 1 * math.sin(math.pi * ((patterncount * 3 + (90 * (i - 1))) / 180))
            dx *= speed
            dy *= speed
            m = Bullet((x, y), (dx, dy))
            gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(4)
    elif pattern == 6:
        for i in range(1,5):
            dx = 1 * math.cos(math.pi * ((patterncount * -3 + (-90 * (i - 1))) / 180))
            dy = 1 * math.sin(math.pi * ((patterncount * -3 + (-90 * (i - 1))) / 180))
            dx *= speed
            dy *= speed
            m = Bullet((x, y), (dx, dy))
            gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(4)
    elif pattern == 7:
        px, py = Player.player.pos
        ax = get_canvas_width() // 2 - px
        ay = get_canvas_height() // 2 - py
        angle = math.atan2(ay,ax) * 180 / math.pi + 180
        dx = 1 * math.cos(math.pi * (angle / 180))
        dy = 1 * math.sin(math.pi * (angle / 180))
        dx *= speed
        dy *= speed
        m = Bullet((x, y), (dx, dy))
        gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(1)
    elif pattern == 8:
        randomset = random.randint(1, 360)
        dx = 1 * math.cos(math.pi * (randomset / 180))
        dy = 1 * math.sin(math.pi * (randomset / 180))
        dx *= speed
        dy *= speed
        m = Bullet((x, y), (dx, dy))
        gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(1)
    elif pattern == 9:
        for i in range(1,5):
            randomset = random.randint(1, 360)
            dx = 1 * math.cos(math.pi * (randomset / 180))
            dy = 1 * math.sin(math.pi * (randomset / 180))
            dx *= speed
            dy *= speed
            m = Bullet((x, y), (dx, dy))
            gfw.world.add(gfw.layer.bullet, m)
        Player.player.apply_patterncount(4)

    if pattern == 3 or pattern == 4 or pattern == 5 or pattern == 6 or pattern == 9:
        if Player.player.patterncount >= 720:
            Player.player.change_pattern()
    else:
        if Player.player.patterncount >= 240:
            Player.player.change_pattern()
    

def generate_bonus():
    x, y, dx, dy = get_border_coords()
    Bonus = random.choice([Bluefairy, Purplefairy])    
    m = Bonus((x, y), (dx, dy))
    gfw.world.add(gfw.layer.bonus, m)

def update():
    turn = Player.player.turn
    if turn % 10 == 0:
        generate()
    Player.player.apply_turn()
    
    score = Player.player.score
    fairy_count = MAX_FAIRY_COUNT + score // 50
    if gfw.world.count_at(gfw.layer.bonus) < fairy_count:
        generate_bonus()  
