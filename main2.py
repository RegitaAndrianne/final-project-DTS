import pygame
pygame.init()

from random import randint

# background/screen
screen_width = 1080
screen_height = 720
display_output = [screen_width,screen_height]
screen = pygame.display.set_mode((display_output),pygame.RESIZABLE)
background = pygame.image.load("images/ocean.jpg").convert()

# set the clock 
clock = pygame.time.Clock()

# display name
pygame.display.set_caption("Collect the Trash")

# import and initialize plastic
plastic = pygame.image.load("images/plastic3.png").convert_alpha()
x = randint(0, screen_width)
y = 0
radius = 100 # plastic width
plastic_rep_x = x + 50 # keep the plastic in range x
print("plastic in x: " + str(plastic_rep_x))
plastic_rep_y = y + 50 # keep the plastic in range y
print("plastic in y: " + str(plastic_rep_y))
speed = 3

# import player and set initialization
player = pygame.image.load("images/diver2.png").convert_alpha()
player_width = 125
player_pos_x = 450
player_pos_y = 500
player_speed = 8
player_rep_x = [player_pos_x + 31, player_pos_x + 94] # region to score 481,494
print("player_rep_x: " + str(player_rep_x))
player_rep_y = [player_pos_y + 14, player_pos_y + 20] #region to score 514,520
print("player_rep_y: " + str(player_rep_y))

# initialitation text score, size and font
black = (0, 0, 0)
text_x = 15
text_y = 15
font = pygame.font.Font("freesansbold.ttf", 40)

#background music
bg_music = pygame.mixer.Sound("sounds/theme-song2.ogg")
bg_music.play(-1)

#sound effect
ting = pygame.mixer.Sound("sounds/cling.wav")

play = True
score = 0

# 1 event screen/play 
def check_for_event(): 
    global play, player_pos_x, player_pos_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos_x += player_speed

# 2 show images
def show_images():
    screen.blit(plastic,(x,y))
    screen.blit(player, (player_pos_x, player_pos_y))

# 3 update position plastic
def update_pos_plastic():
    global y, plastic_rep_x, plastic_rep_y
    y += speed
    plastic_rep_x = x + 50
    #print("update plastic x: " +str(plastic_rep_x))
    plastic_rep_y = y + 50
    #print("update plastic y: " + str(plastic_rep_y))
    initialise_plastic()

# 4 initialize plastic
def initialise_plastic():
    global x, y
    if y > screen_height - radius:
        y = 0
        x = randint(0, screen_width)

# 5 border to keep plastic image in screen width
def enforce_border():
    global x, y, player_pos_x, player_pos_y
    if x < 0:
        x = 0
    if x > screen_width - radius:
        x = screen_width - radius
    if y > screen_height - radius:
        y = screen_height - radius
    
    if player_pos_x < 0:
        player_pos_x = 0
    if player_pos_x > screen_width - player_width:
        player_pos_x = screen_width - player_width

# count score or reset
def check_for_score():
    global score
    if plastic_rep_x in range(player_rep_x[0], player_rep_x[1]) or plastic_rep_y in range (player_rep_y[0], player_rep_y[1]):
        score += 1
        ting.play()
        print("plastic_rep_x: " + str(plastic_rep_x))
        print("plastic_rep_y: " + str(plastic_rep_y))
    elif plastic_rep_y in range(player_rep_y[0], player_rep_y[1]) and plastic_rep_x not in range (player_rep_x[0], player_rep_x[1]):
        score = 0


# display score
def show_score():
    score_display = font.render("Score " + str(score), True, black)
    screen.blit(score_display, (text_x, text_y))


#-------------------------------------------LOOP GAME--------------------------------------------------------------

while play:
    clock.tick(60)
    screen.blit(background,(0,0))
    check_for_event()
    update_pos_plastic()
    enforce_border()
    show_images()
    check_for_score()
    show_score()
    pygame.display.flip()
pygame.quit()
