import pygame
import os
import time
import math
import pygame.display
import pygame.transform
import random

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
pygame.display.update()

class link():
#    def __init__(self,size,x,y,shter):
    def __init__(self,size,x,y,head):
        self.x=x
        self.y=y
        self.xvelo=1
        self.yvelo=0
        self.size=round(size)
        self.mass=self.size**2
        self.shape=pygame.image.load("scale2.png")
        if head==True:
            self.shape=pygame.image.load("head.png")
        self.shape=pygame.transform.scale(self.shape, (self.size,self.size))
        self.direction=0
    def draw(self,pointer):
        shape2=pygame.transform.rotate(self.shape,pointer)
        self.direction=pointer
        while self.direction<0:
            self.direction+=360
        self.direction=self.direction%360            
        pointer=pointer%90
        pointer=pointer*math.pi/180
        screen.blit(shape2,(self.x-(self.size*math.cos((math.pi/4-pointer)))/math.sqrt(2),self.y-self.size*math.sin(pointer)-self.size*(math.sin(math.pi/4-pointer)/math.sqrt(2))))
    def spitfire(self):
        for e in range(1,100):
            leftright=random.randint(0,1)
            leftright-=0.5
            leftright*=2
            gamma=flame(leftright*(400/(0.3*random.randint(0,45)+6.6)-20),random.randint(1,300),random.randint(1,8))
            flames.append(gamma)



        

class flame():
    def __init__(self,angle,distance,strength):
        self.angle=angle
        self.distance=distance
        self.strength=strength
        self.colour=(255,strength*0.09*(330-distance),0)
    def draw(self,x,y,diction,num):
        direction=diction+90
        pygame.draw.rect(screen,self.colour,(x+100*math.cos(math.pi*direction/180)+self.distance*math.cos(math.pi*(direction+self.angle)/180),y-100*math.sin(math.pi*direction/180)-self.distance*math.sin(math.pi*(direction+self.angle)/180),5,5))
        self.strength-=1
        if self.strength==0:
            flames.pop(num)
        else:
            self.colour=(255,self.strength*0.09*(330-self.distance),0)

            
class wings():
    def __init__(self,wingsize):
        self.wings=pygame.image.load("wings.png")
        self.wingsize=wingsize
        self.wings=pygame.transform.scale(self.wings,(self.wingsize,self.wingsize))
    def draw(self,pointer,x,y):
        wings=pygame.transform.rotate(self.wings,pointer)
        pointer=pointer%90
        pointer=pointer*math.pi/180
        screen.blit(wings,(x-(self.wingsize*math.cos((math.pi/4-pointer)))/math.sqrt(2),y-self.wingsize*math.sin(pointer)-self.wingsize*(math.sin(math.pi/4-pointer)/math.sqrt(2)))) 

clock=pygame.time.Clock()
zoom=wings(1000)
zoomy=wings(500)
scales=[]
middles=[]
flames=[]
factor=0.01
numcircles=10
zoomer=round(numcircles/3)
zoomyer=round(numcircles/2)
potato=1
turning=0
tracker=0
done=False
torchem=False
maindirection=0
flying=0
counta=0
head=True

for i in range (0,numcircles):
    alpha = link(200-16*i,1000-100*i,500,head)
    scales.append(alpha)
    head=False

while tracker<numcircles/3:
    first=scales[tracker]
    second=scales[tracker+1]
    beta = link((first.size+second.size)/2,500,500,head)
    middles.append(beta)
    tracker+=1
tracker=0

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                turning-=0.08
            if event.key == pygame.K_d:
                turning+=0.08
            if event.key == pygame.K_f:
                torchem=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                turning+=0.08
            if event.key == pygame.K_d:
                turning-=0.08
            if event.key == pygame.K_f:
                torchem=False
                flames.clear()

    for i in scales:
        if potato==1:
            maindirection+=turning
            i.xvelo=20*math.cos(maindirection)
            i.yvelo=20*math.sin(maindirection)
            i.draw(-90-maindirection*180/math.pi)
            if torchem==True:
                i.spitfire()
                counta=0
                for f in flames:
                    f.draw(i.x,i.y,i.direction,counta)
                    counta+=1
        elif potato==numcircles:
            prevdude=scales[potato-2]
            prevdistance=math.sqrt((i.x-prevdude.x)**2+(i.y-prevdude.y)**2)
            if prevdude.x==i.x:
                i.x+=0.001
            if prevdude.x-i.x>0:
                prevang=math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            else:
                prevang=math.pi+math.atan((i.y-prevdude.y)/(prevdude.x-i.x))
            i.xvelo+=0.2*(math.cos(prevang)*(prevdistance-((i.size+prevdude.size)*factor)))
            i.yvelo+=-0.2*(math.sin(prevang)*(prevdistance-((i.size+prevdude.size)*factor)))
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
            i.xvelo=0.4*(math.cos(prevang)*(prevdistance-((i.size+prevdude.size)*factor))+math.cos(nextang)*(nextdistance-((i.size+prevdude.size)*factor)))
            i.yvelo=-0.4*(math.sin(prevang)*(prevdistance-((i.size+prevdude.size)*factor))+math.sin(nextang)*(nextdistance-((i.size+prevdude.size)*factor)))
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
        if potato==zoomer:
            zoom.draw(i.direction,i.x,i.y)
        if potato==zoomyer:
            zoomy.draw(i.direction,i.x,i.y)

    for j in middles:
        first=scales[tracker]
        second=scales[tracker+1]
        j.x=(first.x+second.x)/2
        j.y=(first.y+second.y)/2
        j.direction=(first.direction+second.direction)/2
        if (first.direction-second.direction)**2>32400:
            j.direction+=180
        j.draw(j.direction)
        tracker+=1
    potato=1
    tracker=0
    pygame.display.update()
    clock.tick()
    print(clock.get_fps())
    screen.fill(BLACK)
print(len(scales))
print(len(middles))

