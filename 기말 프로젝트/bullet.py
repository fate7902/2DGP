from pico2d import *
import gfw

MOVE_PPS = 200

class Bullet:
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/bullet.png')
        
    def init(self, pos, delta, imageName):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load(imageName)

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        if x < -self.image.w or x > get_canvas_width() + self.image.w or y < -self.image.h or y > get_canvas_height() + self.image.h:
            gfw.world.remove(self)
        self.pos = x, y

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def draw(self):        
        self.image.draw(*self.pos)
