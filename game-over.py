import pygame
from random import randint

pygame.init()

# draw screen, name, clock
screen = pygame.display.set_mode((1080,720), pygame.RESIZABLE) #screen size
screen_width = 1080
screen_height = 720
pygame.display.set_caption('Collect the Trash') #window title
clock = pygame.time.Clock() 
# FPS = 120

#background
court = pygame.image.load('images/ocean.jpg').convert()

#text for score
text_x = 15
text_y = 15
font = pygame.font.Font("freesansbold.ttf", 40)

#diver or player
diver = pygame.image.load('images/diver-down.png').convert_alpha()
diver_width = 189
diver_pos_x = 500
diver_pos_y = 550
diver_rep_x = [diver_pos_x +31, diver_pos_x+94] 
diver_rep_y = [diver_pos_y+14, diver_pos_y+20]

diver_speed = 2  #driver speed movement

#object plastic
plastic = pygame.image.load('images/plastic.png').convert_alpha()
x = randint(0, screen_width)
y = 0
radius = 189
plastic_rep_x = x
plastic_rep_y = y
speed = 1 #speed of the plastic fall

play = True

#background music
bg_music = pygame.mixer.Sound("sounds/theme-song2.ogg")
bg_music.play(-1)

#sound effect
ting = pygame.mixer.Sound("sounds/cling.wav")

#score
score = 0

def check_for_event():
    global play, diver_pos_x, diver_pos_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    #cursor, diver movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        diver_pos_x -= diver_speed
    if keys[pygame.K_RIGHT]:
        diver_pos_x += diver_speed

#show all image
def show_images():
    global diver_rep_x, diver_rep_y
    screen.blit(plastic, (x,y))
    screen.blit(diver, (diver_pos_x, diver_pos_y))
    diver_rep_x = [diver_pos_x +31, diver_pos_x+94] 
    diver_rep_y = [diver_pos_y+14, diver_pos_y+20]

#plastic movement
def update_plastic_pos():
    global y, plastic_rep_x, plastic_rep_y
    y += speed
    plastic_rep_x = x + 50
    plastic_rep_y = y + 50
    initialise_plastic()

def initialise_plastic():
    global x, y
    if y > screen_height - radius:
        y = 0
        x = randint(0, screen_width)

#so the plastic stay on the display/window
def enforce_border():
    global x, y, diver_pos_x, diver_pos_y 
    if x < 0:
        x = 0
    if x > screen_width - radius:
        x = screen_width - radius
    if y < 0:
        y = 0
    if y > screen_height - radius:
        y = screen_height - radius
#so the diver stay on the display/window    
    if diver_pos_x < 0:
        diver_pos_x = 0
    if diver_pos_x > screen_width - diver_width:
        diver_pos_x = screen_width - diver_width


def check_for_score():
    global score
    if plastic_rep_x in range(diver_rep_x[0], diver_rep_x[1]) and plastic_rep_y in range(diver_rep_y[0], diver_rep_y[1]): 
        score += 1
        ting.play() #sound effect
    elif plastic_rep_y in range(diver_rep_y[0], diver_rep_y[1]) and plastic_rep_y not in range(diver_rep_x[0], diver_rep_x[1]): 
        score = 0


#display score
def show_score():
    score_disp = font.render("SCORE: " + str(score), True, (0, 0, 0))
    screen.blit(score_disp, (text_x, text_y))
    # print(score)


#main loop
while play:
    clock.tick()
    screen.blit(court,(0,0))
    check_for_event() 
    update_plastic_pos() #plastic movement
    enforce_border() 
    show_images()
    check_for_score()
    show_score()
    pygame.display.flip()

pygame.quit()
