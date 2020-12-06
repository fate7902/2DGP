import random
from pico2d import *
import gfw
import gobj

FPS = 12
MOVE_PPS = 200
LINE = 100

class Fairy:
    images = {}
    ACTIONS = ['Idle']
    def __init__(self, pos, delta, mag):
        self.init(pos, delta, 'blue_fairy', 'Idle', mag)
        
    def init(self, pos, delta, imageName, keyword, mag=0):
        self.pos = pos
        self.delta = delta
        self.fidx = 0
        self.time = 0
        self.action = keyword
        self.images = Fairy.load_images(imageName)

    @staticmethod
    def load_images(char):
        if char in Fairy.images:
            return Fairy.images[char]

        images = {}
        count = 0
        file_fmt = '%s/%s_%d.png'
        for action in Fairy.ACTIONS:
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
        Fairy.images[char] = images        
        return images

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * FPS)
        x, y = self.pos
        dx, dy = self.delta
        
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        if x < -LINE or x > get_canvas_width() + LINE or y < -LINE or y > get_canvas_height() + LINE:
            gfw.world.remove(self)
        self.pos = x, y

    def draw(self):        
        self.image.composite_draw(0, '', *self.pos, 10, 10)

class Bluefairy(Fairy):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'blue_fairy', 'Idle', 0)
        self.score = 5

    def get_bb(self):
        self.action = 'Idle'
        images = self.images[self.action]        
        image = images[self.fidx % len(images)]
        hw = image.w // 2
        hh = image.h // 2
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def draw(self):
        dx, dy = self.delta
        self.action = 'Idle'
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if dx > 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w, image.h)

class Purplefairy(Fairy):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'purple_fairy', 'Idle', 0)
        self.score = 8

    def get_bb(self):
        self.action = 'Idle'
        images = self.images[self.action]        
        image = images[self.fidx % len(images)]
        hw = image.w // 2
        hh = image.h // 2
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def draw(self):
        dx, dy = self.delta
        self.action = 'Idle'
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if dx > 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w, image.h)
