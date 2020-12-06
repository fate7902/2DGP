import random
from pico2d import *
import gfw
import gobj

FPS = 12

class Bulletzone:
    images = {}
    ACTIONS = ['Idle']
    def __init__(self):        
        self.images = Bulletzone.load_images('bullet_zone')
        self.action = 'Idle'
        self.fidx = 0
        self.time = 0
        
        self.reset()

        Bulletzone.bulletzone = self

    @staticmethod
    def load_images(char):
        if char in Bulletzone.images:
            return Bulletzone.images[char]

        images = {}
        count = 0
        file_fmt = '%s/%s_%d.png'
        for action in Bulletzone.ACTIONS:
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
        Bulletzone.images[char] = images        
        return images
    
    def reset(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        
    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * FPS)

    def draw(self):
        self.action = 'Idle'
        images = self.images[self.action]
        image = images[self.fidx % len(images)]        
        image.composite_draw(0, '', *self.pos, image.w * 2, image.h * 2)
