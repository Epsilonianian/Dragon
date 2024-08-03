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

scale = pygame.image.load("blue.png")
pygame.display.update()

class link():
    def __init__(self,size,x,y):
        self.x=x
        self.y=y
        self.displayx=x
        self.displayy=y
        self.size=round(size)
        self.direction=225
        self.shape=pygame.transform.scale(scale, (50,50))
    def draw(self):
        shape2=pygame.transform.rotate(self.shape,self.direction)
        screen.blit(shape2,(self.displayx,self.displayy))
        screen.blit

scales=[]

for i in range (1,10):
    alpha = link(200-1.65**i,1300-50*i,500-50*i)
    print(100-1.5**i)
    scales.append(alpha)

potato=0
maindirection=math.pi*0.25
turning=0
prevx=0
prevy=0
tracker=0
done=False
while not done:
    tracker+=1
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                turning-=0.02
            if event.key == pygame.K_d:
                turning+=0.02
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                turning+=0.02
            if event.key == pygame.K_d:
                turning-=0.02
    maindirection+=turning

    for i in scales:
        if potato==0:
            scaledirection=maindirection
            i.direction=270-180*scaledirection/math.pi
            i.x+=math.cos(scaledirection)*2
            i.y+=math.sin(scaledirection)*2
            i.displayx=i.x
            i.displayy=i.y
        else:
            if i.x-prevx!=0:
                scaledirection=math.pi/2+math.atan((i.y-prevy)/(i.x-prevx))
            else:
                scaledirection=math.pi/2+math.atan((i.y-prevy)/(0.00001+i.x-prevx))
            if i.x-prevx>0:
                scaledirection+=math.pi
            scaledirection*=-1
            i.x=prevx-math.sin(scaledirection)*2
            i.y=prevy-math.cos(scaledirection)*2
            i.displayx=prevx-math.sin(scaledirection)*50*potato
            i.displayy=prevy-math.cos(scaledirection)*50*potato
            i.direction=-180*(math.pi/2+math.atan((i.displayy-prevy)/(i.displayx-prevx)))/math.pi
        potato+=1




        i.draw()
        prevx=i.x
        prevy=i.y
    potato=0
    pygame.display.update()
    clock.tick(50)
    if tracker%10==0:
        screen.fill(BLACK)
print(len(scales))