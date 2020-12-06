import random
from pico2d import *
import gfw
import gobj

FPS = 12
MOVE_PPS = 300
MAX_LIFE = 5
SCORE_TEXT_COLOR = (255, 255, 255)

class Player:
    images = {}
    ACTIONS = ['Idle', 'Walk']
    def __init__(self):        
        self.idleimages = Player.load_images('player_idle')
        self.walkimages = Player.load_images('player_walk')
        self.action = 'Idle'
        self.fidx = 0
        self.time = 0
        self.direction = 1
        
        #self.font = gfw.font.load('res/ConsolaMalgun.ttf', 35)        
        #self.radius = self.image.h // 2        
        #self.heart_red = gfw.image.load('res/heart_red.png')
        #self.heart_white = gfw.image.load('res/heart_white.png')
        self.reset()
        
        #global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP
        #BOUNDARY_LEFT = self.image.w // 2
        #BOUNDARY_DOWN = self.image.h // 2
        #BOUNDARY_RIGHT = get_canvas_width() - BOUNDARY_LEFT
        #BOUNDARY_UP = get_canvas_height() - BOUNDARY_DOWN

        Player.player = self

    @staticmethod
    def load_images(char):
        if char in Player.images:
            return Player.images[char]

        images = {}
        count = 0
        file_fmt = '%s/%s_%d.png'
        for action in Player.ACTIONS:
            action_images = []
            n = 1
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Player.images[char] = images        
        return images
    
    def reset(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.dx, self.dy = 0, 0
        self.life = MAX_LIFE
        self.score = 0
        self.pattern = 1
        self.patterncount = 0
        self.turn = 10
        #self.pattern = random.randint(1, 4)
        
    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * FPS)
        self.score += gfw.delta_time
        x,y = self.pos
        x += self.dx * MOVE_PPS * gfw.delta_time
        y += self.dy * MOVE_PPS * gfw.delta_time
        #x = clamp(BOUNDARY_LEFT, x, BOUNDARY_RIGHT)
        #y = clamp(BOUNDARY_DOWN, y, BOUNDARY_UP)
        self.pos = x, y

    def draw(self):
        if self.dx == 0 and self.dy == 0:
            self.action = 'Idle'
            images = self.idleimages[self.action]
        else:
            self.action = 'Walk'
            images = self.walkimages[self.action]        
        image = images[self.fidx % len(images)]
        flip = 'h' if self.direction != 1 else ''
        image.composite_draw(0, flip, *self.pos, image.w // 3, image.h // 3)

    #def draw(self):
        #self.image.draw(*self.pos)
        #x = get_canvas_width() - 30
        #y = get_canvas_height() - 30
        #for i in range(MAX_LIFE):
            #heart = self.heart_red if i < self.life else self.heart_white
            #heart.draw(x, y)
            #x -= heart.w
        #pos = 30, get_canvas_height() - 30
        #self.font.draw(*pos, 'Score: %.1f' % self.score, SCORE_TEXT_COLOR)

    def apply_item(self, item):
        if self.life == MAX_LIFE:
            self.score += item.score
            return True
        self.life += 1
        return False

    def decreate_life(self):
        self.life -= 1
        return self.life <= 0

    def get_bb(self):
        if self.dx == 0 and self.dy == 0:
            self.action = 'Idle'
            images = self.idleimages[self.action]
        else:
            self.action = 'Walk'
            images = self.walkimages[self.action]        
        image = images[self.fidx % len(images)]
        hw = image.w // 9
        hh = image.h // 10
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def change_pattern(self):
        self.pattern = 2
        #self.pattern = random.randint(1, 4)

    def apply_patterncount(self):
        self.patterncount += 1

    def apply_turn(self):
        self.turn += 1

    def handle_event(self, e):
        global dx,dy,direction
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 1
                self.direction = 1
            elif e.key == SDLK_RIGHT:
                self.dx += 1
                self.direction = 2
            elif e.key == SDLK_DOWN:
                self.dy -= 1
            elif e.key == SDLK_UP:
                self.dy += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 1
            elif e.key == SDLK_RIGHT:
                self.dx -= 1
            elif e.key == SDLK_DOWN:
                self.dy += 1
            elif e.key == SDLK_UP:
                self.dy -= 1
