import pygame
import os
import time
import math
import pygame.display
pygame.init() 
os.chdir(os.path.dirname(__file__))

font = pygame.font.SysFont('Calibri', 25, True, False)

##### Colours ##### 
BLACK = (  0,   0,   0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
PURPLE = (255, 0, 255)

##### Screen Initialisation ##### 
SCREEN_WIDTH = 1800 
SCREEN_HEIGHT = 1000 
screensize = (SCREEN_WIDTH, SCREEN_HEIGHT) 
screen = pygame.display.set_mode(screensize) 
pygame.display.set_caption("Dragoon") 
centering=0
done = False               
movingVertically=False
clock = pygame.time.Clock() 

scale = pygame.image.load("scale.png")
pygame.display.update()
