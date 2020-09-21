from pico2d import *
import helper

def handle_events():
    global running, dx,dy, x, y, target, speed
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                if speed > 0:
                    speed += 1
                    dx,dy = helper.delta((x,y),target[0],speed)
            elif e.button == SDL_BUTTON_RIGHT:
                if speed == 0:
                    speed += 1
                target.append((e.x,get_canvas_height() - e.y - 1))
                dx,dy = helper.delta((x,y),target[0],speed)                
    if speed > 0:
        (x,y),done = helper.move_toward((x,y),(dx,dy),target[0])        
        if done == True:
            dx,dy = 0,0
            del target[0]
            if not target:
                speed = 0
            else:
                dx,dy = helper.delta((x,y),target[0],speed)                
                
                    
open_canvas()

gra=load_image('../res/grass.png')
ch=load_image('../res/run_animation.png')

running = True
done = False
target = []
x,y = 400,85
dx,dy = 0,0
speed = 0
fidx = 0
while running:
    clear_canvas()
    gra.draw(400,30)    
    ch.clip_draw(fidx*100,0,100,100,x,y)
    update_canvas() 

    handle_events()
    
    x += dx
    y += dy
    fidx = (fidx + 1) % 8 

    delay(0.01)        

close_canvas()
