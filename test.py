import pygame
pygame.init()

# Create screen size
SCREEN = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
# SCREEN = pygame.display.set_mode([626,417],pygame.RESIZABLE)

# Name of window
pygame.display.set_caption('Project Game')

clock = pygame.time.Clock()

# load the sound
click_sound = pygame.mixer.Sound("sounds/ES_Love Card-MarcTorch.mp3")


# background position
background_position = [0,0]

# load and set up graphics
background_image = pygame.image.load("images/bg_2.jpg").convert()
player_image = pygame.image.load("images/diver-up.png").convert_alpha()

# Visible cursor
pygame.mouse.set_visible(False)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    # copy image to screen
    SCREEN.blit(background_image,background_position)

    # current mouse position
    player_position = pygame.mouse.get_pos()
    # set_mouse_speed = 
    x = player_position[0]
    y = player_position[1]
    # player_rect = player_image.get_rect(center = (300,321))


    # copy player image to screen
    SCREEN.blit(player_image, [x,y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()