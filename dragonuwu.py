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

class link():
    def __init__(self,size,x,y):
        self.x=x
        self.y=y
        self.xvelo=0
        self.yvelo=0
        self.size=round(size)
        self.mass=self.size**2
        self.shape=pygame.transform.scale(scale, (self.size,self.size))
    def draw(self):
        if self.xvelo==0:
            shape2=pygame.transform.rotate(self.shape,-90+(180*(math.atan(-self.yvelo/(self.xvelo+0.0001))))/math.pi)
        if self.xvelo>0:
            shape2=pygame.transform.rotate(self.shape,-90+(180*(math.atan(-self.yvelo/(self.xvelo))))/math.pi)
        if self.xvelo<0:
            shape2=pygame.transform.rotate(self.shape,90+(180*(math.atan(-self.yvelo/(self.xvelo))))/math.pi)

        screen.blit(shape2,(self.x,self.y))

scales=[]
numcircles=5
potato=1
turning=0
tracker=0
done=False
maindirection=0
for i in range (0,numcircles):
    alpha = link(200-1.65**i,1300-50*i,500-50*i)
    scales.append(alpha)


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

    for i in scales:
        if potato==1:
            maindirection+=turning
            i.xvelo=5*math.cos(maindirection)
            i.yvelo=5*math.sin(maindirection)
        elif potato==numcircles:
            prevdude=scales[potato-2]
            prevdistance=math.sqrt((i.x-prevdude.x)**2+(i.y-prevdude.y)**2)
            if prevdude.x==i.x:
                i.x+=0.001
            if prevdude.x-i.x>0:
                prevang=math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            else:
                prevang=math.pi+math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            i.xvelo+=100*(math.cos(prevang)*(prevdistance-i.size-prevdude.size))/i.mass
            i.yvelo+=100*(math.sin(prevang)*(prevdistance-i.size-prevdude.size))/i.mass
            print((math.cos(prevang)*(prevdistance-i.size-prevdude.size))/i.mass)
        else:
            prevdude=scales[potato-2]
            print(potato-2)
            nextdude=scales[potato]
            prevdistance=math.sqrt((i.x-prevdude.x)**2+(i.y-prevdude.y)**2)
            nextdistance=math.sqrt((i.x-nextdude.x)**2+(i.y-nextdude.y)**2)
            if prevdude.x==i.x:
                i.x+=0.001
            if prevdude.x-i.x>0:
                prevang=math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            else:
                prevang=math.pi+math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            if nextdude.x==i.x:
                i.x+=0.001
            if nextdude.x-i.x>0:
                nextang=math.atan((i.y-nextdude.y)/(nextdude.x-i.x))
            else:
                nextang=math.pi+math.atan((i.y-nextdude.y)/(nextdude.x-i.x))
            i.xvelo+=100*(math.cos(prevang)*(prevdistance-i.size-prevdude.size)+math.cos(nextang)*(nextdistance-i.size-nextdude.size))/i.mass
            i.yvelo+=100*(math.sin(prevang)*(prevdistance-i.size-prevdude.size)+math.sin(nextang)*(nextdistance-i.size-nextdude.size))/i.mass
        potato+=1
        i.x+=i.xvelo
        i.y+=i.yvelo
        i.draw()
    potato=1
    pygame.display.update()
    clock.tick(1)
    screen.fill(BLACK)
print(len(scales))