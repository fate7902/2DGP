import gfw
from pico2d import *
import gobj
from player import Player
from fairy import Fairy
import objgen
import highscore
from bulletzone import Bulletzone
from background import Background,HorzScrollBackground

canvas_width = 1740
canvas_height = 942

STATE_IN_GAME, STATE_GAME_OVER = range(2)

def enter():
    gfw.world.init(['bg1', 'bulletzone', 'bullet', 'bonus', 'bg2', 'player', 'ui'])
    objgen.init()
    
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

    highscore.load()

    global music_bg
    music_bg = load_music('res/bgm_fullMoonParty.mp3')
    music_bg.repeat_play()

    global game_state
    game_state = STATE_IN_GAME

    global game_over_image
    game_over_image = gfw.image.load('res/game_over.png')

    start_game()

def start_game():
    global game_state
    game_state = STATE_IN_GAME

    player.reset()
    gfw.world.clear_at(gfw.layer.bullet)
    gfw.world.clear_at(gfw.layer.bonus)
    gfw.world.remove(highscore)

    music_bg.repeat_play()

def end_game():
    global game_state
    game_state = STATE_GAME_OVER
    music_bg.stop()
    highscore.add(player.score)
    gfw.world.add(gfw.layer.ui, highscore)

def update():
    global game_state
    if game_state != STATE_IN_GAME:
        return
    
    gfw.world.update()
    objgen.update()

    for o in gfw.world.objects_at(gfw.layer.bullet):
        if collides_distance(o, player):
            gfw.world.remove(o)
            #sound_explosion.play()
            dead = player.decreate_life()
            if dead:
                end_game()                

    for o in gfw.world.objects_at(gfw.layer.bonus):
        if collides_distance(o, player):
            gfw.world.remove(o)
            #sound_item.play()
            player.apply_item(o)

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    if game_state == STATE_GAME_OVER:
        x = get_canvas_width() // 2
        y = get_canvas_height() * 2 // 3
        game_over_image.draw(x, y, get_canvas_width() // 2, get_canvas_height() // 2)

def collides_distance(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    
    return True    

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            if game_state == STATE_GAME_OVER:
                start_game()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
