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
#    def __init__(self,size,x,y,shter):
    def __init__(self,size,x,y):
        self.x=x
        self.y=y
        self.xvelo=1
        self.yvelo=0
        self.size=round(size)
        self.mass=self.size**2
        self.shape=pygame.image.load("scale.png")
#        self.shape=pygame.image.load(f"{shter}.png")
        self.shape=pygame.transform.scale(self.shape, (self.size,self.size))
    def draw(self,pointer):
        shape2=pygame.transform.rotate(self.shape,pointer)
        pointer=pointer%90
        pointer=pointer*math.pi/180
        screen.blit(shape2,(self.x-(self.size*math.cos((math.pi/4-pointer)))/math.sqrt(2),self.y-self.size*math.sin(pointer)-self.size*(math.sin(math.pi/4-pointer)/math.sqrt(2))))
#        pygame.draw.rect(screen,RED,pygame.Rect(900,500,self.size,self.size),2)


scales=[]
factor=0.1
numcircles=8
potato=1
turning=0
tracker=0
done=False
maindirection=0
for i in range (0,numcircles):
    alpha = link(200-1.9*i,500,500)
#    alpha = link(50-2*i,500,500,i+1)
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
            i.draw(-90-maindirection*180/math.pi)
        elif potato==numcircles:
            prevdude=scales[potato-2]
            prevdistance=math.sqrt((i.x-prevdude.x)**2+(i.y-prevdude.y)**2)
            if prevdude.x==i.x:
                i.x+=0.001
            if prevdude.x-i.x>0:
                prevang=math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            else:
                prevang=math.pi+math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            i.xvelo+=0.1*(math.cos(prevang)*(prevdistance-((i.size+prevdude.size)*factor)))
            i.yvelo+=-0.1*(math.sin(prevang)*(prevdistance-((i.size+prevdude.size)*factor)))
        else:
            prevdude=scales[potato-2]
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
            i.xvelo=0.2*(math.cos(prevang)*(prevdistance-((i.size+prevdude.size)*factor))+math.cos(nextang)*(nextdistance-((i.size+prevdude.size)*factor)))
            i.yvelo=-0.2*(math.sin(prevang)*(prevdistance-((i.size+prevdude.size)*factor))+math.sin(nextang)*(nextdistance-((i.size+prevdude.size)*factor)))
            if i.x-prevdude.x==0:
                direction=90+(180*(math.atan((i.y-prevdude.y)/(prevdude.x-i.x+0.0001))))/math.pi
            if i.x-prevdude.x>0:
                direction=90+(180*(math.atan((i.y-prevdude.y)/(prevdude.x-i.x))))/math.pi
            if i.x-prevdude.x<0:
                direction=-90+(180*(math.atan((i.y-prevdude.y)/(prevdude.x-i.x+0.0001))))/math.pi
            i.draw(direction)
        potato+=1
        i.x+=i.xvelo
        i.y+=i.yvelo
    potato=1
    pygame.display.update()
    clock.tick(100)
    screen.fill(BLACK)
print(len(scales))