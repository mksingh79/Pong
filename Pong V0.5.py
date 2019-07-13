# Pong :))

import simplegui
RADIUS = 20
WIDTH = 400
HEIGHT = 400 
BALL_POS = [WIDTH/2, HEIGHT/2]    # initial ball position
point_one = [(WIDTH/2)-60,HEIGHT] # paddle of size 100 pixels
point_two = [(WIDTH/2)+60,HEIGHT]
VEL_BALL = [0,0]
VEL_PADDLE = [0,0]
score = 0
last_score = 0
best_score = 0
game_text = 'Press 1 to start'

#draw handler
def draw_handler(canvas):
    global WIDTH, point_one,point_two,last_score,score,BALL_POS,game_text,VEL_BALL
    
    #Ball position
    BALL_POS[0] += VEL_BALL[0]
    BALL_POS[1] += VEL_BALL[1]
    
    #paddle position
    point_one[0] += VEL_PADDLE[0]
    point_two[0] += VEL_PADDLE[1]
    
    #prevent paddle from moving beyond the canvas
    if point_one[0] < 0:
        point_one = [0, HEIGHT]
        point_two = [120, HEIGHT]
    if point_two[0] > WIDTH:
        point_one = [WIDTH-120, HEIGHT]
        point_two = [WIDTH, HEIGHT]
    
    #collision with walls
    if BALL_POS[0] <= RADIUS: 			#reached left wall
        VEL_BALL[0] = -VEL_BALL[0]
    elif BALL_POS[0] >= WIDTH-RADIUS:	#reached right wall
        VEL_BALL[0] = -VEL_BALL[0]
    elif BALL_POS[1] <= RADIUS:			#reached top wall
        VEL_BALL[1] = -VEL_BALL[1]
    elif BALL_POS[1] >= HEIGHT-RADIUS and (BALL_POS[0] > point_one[0] and BALL_POS[0] < point_two[0]) :	#reached paddle
        print 'paddle hit'
        print BALL_POS,point_one,point_two
        VEL_BALL[1] += 0.5				#increase speed after every paddle hit
        VEL_BALL[1] = -VEL_BALL[1]
        score += 1
    elif BALL_POS[1] > HEIGHT:          # reset ball position if it goes down
        BALL_POS = [WIDTH/2, HEIGHT/2]
        VEL_BALL = [0,0]
        game_text = 'Game Over! Try again'
        last_score = score
        score = 0
        point_one = [(WIDTH/2)-60,HEIGHT] # paddle of size 100 pixels
        point_two = [(WIDTH/2)+60,HEIGHT]
           
    canvas.draw_circle(BALL_POS, RADIUS,2,'Red','White')
    canvas.draw_line(point_one,point_two, 10, 'White')
    canvas.draw_text('Points:'+ str(score), [300,20], 20, 'White')
    canvas.draw_text(game_text, [140,100], 20, 'Green')
    canvas.draw_text('Last score:'+ str(last_score), [20,20], 20, 'White')
    
#Move paddle notice the use of keydown and key up to maintain speed
def keydown(key):
    global VEL_BALL, game_text
    accel = 3
    
    #start the game
    if key==simplegui.KEY_MAP["1"]: 
        VEL_BALL = [3,4]
        game_text = '' 				#remove game text
        
    if key==simplegui.KEY_MAP["a"] :
        VEL_PADDLE[0] -= accel
        VEL_PADDLE[1] -= accel
    elif key==simplegui.KEY_MAP["d"] :
        VEL_PADDLE[0] += accel
        VEL_PADDLE[1] += accel

def keyup(key):
    accel = 3
    
    if key==simplegui.KEY_MAP["a"]:
        VEL_PADDLE[0] += accel
        VEL_PADDLE[1] += accel
    elif key==simplegui.KEY_MAP["d"] :
        VEL_PADDLE[0] -= accel
        VEL_PADDLE[1] -= accel


#create frame
frame = simplegui.create_frame('Bouncy Ball', WIDTH,HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#start frame
frame.start()