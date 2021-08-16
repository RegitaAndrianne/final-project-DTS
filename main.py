import sys, pygame, pygame.mixer
pygame.init()

# SCREEN = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
SCREEN = pygame.display.set_mode((626,417), pygame.RESIZABLE)

pygame.display.set_caption('Collect the Trash')

bg_underwater = pygame.image.load('images/bg_1.jpg').convert()
diver_up = pygame.image.load('images/diver-up.png').convert_alpha()
# diver_down = pygame.image.load('images/diver-down.png').convert_alpha()
# diver_frames = [diver_down, diver_up]
# diver_index = 0
# diver = diver_frames[diver_index]
# diver_rect = diver_up.get_rect(center = (300,321))

SCREEN.blit(bg_underwater,(0,0))
# SCREEN.blit(diver_up,diver_rect)
# SCREEN.blit(diver_up,[x,y])
pygame.display.update()
game_over = False

clock = pygame.time.Clock()
# FPS = 120


while not game_over:
    clock.tick(120)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # SCREEN.blit(diver_up,diver_rect)
    
    diver_position = pygame.mouse.get_pos()
    print(diver_position)
    x = diver_position[0]
    y = diver_position[1]
    SCREEN.blit(diver_up,[x,y])


    
pygame.quit()
quit()