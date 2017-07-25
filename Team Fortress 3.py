import pygame
import random

WIDTH = 1920 #width of our game window
HEIGHT = 1080 #height of our game window
FPS = 60

#Colors rgb

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initialize and create game window

pygame.init()
pygame.mixer.init() #initializes sound
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #create screen
pygame.display.set_caption("TEAM FORTRESS 3") #gives game a name
clock = pygame.time.Clock() #keep track of speed/time

#Game Loop

running = True
while running:
    clock.tick(FPS) #keep the loop running at the right speed
    #Process Inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Updates
    #Renders (draws)
    screen.fill(BLACK)
    #after drawing everything, flip the display
    pygame.display.flip()
pygame.quit()
