from pico2d import *

def handle_events():
    global running, dx, x, y    
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
        elif e.type == SDL_MOUSEMOTION:
            x,y = e.x,get_canvas_height() - e.y - 1
                    
open_canvas()

gra=load_image('grass.png')
ch=load_image('run_animation.png')

running = True
x,y = 400,85
dx = 0
fidx = 0
while running:
    clear_canvas()
    gra.draw(400,30)
    ch.clip_draw(fidx*100,0,100,100,x,y)
    update_canvas() 

    handle_events()     

    x += dx
    fidx = (fidx + 1) % 8 

    delay(0.01)        

close_canvas()
