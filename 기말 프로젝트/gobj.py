from pico2d import *

RES_DIR = 'res'

class Background:
    def __init__(self):
        self.image = load_image(RES_DIR + '/backgroung_1740x942.png')
    def draw(self):
        self.image.draw(870, 460, 1740,920)
    def update(self):
        pass


if __name__ == "__main__":
    print("Running test code ^_^")
