import pygame
from random import *
pygame.init()

width = 800
vis = 600
fps = 60
tanker=32

window = pygame.display.set_mode((width, vis))
clock = pygame.time.Clock()
directs=[[-1,0],[0,-1],[1,0],[0,1]]

class Tank:
    def __init__(self,color,x,y,direct,lol):
        objects.append(self)
        self.type="tank"
        self.direct=direct
        self.color=color
        self.rect=pygame.Rect(x,y,tanker,tanker)
        self.speed_move=2
        self.damage_pyl = 1
        self.speed_pyl = 5
        self.count = 0
        self.dayn = 60
        self.helf = 5#


        self.key_left=lol[0]
        self.key_up=lol[1]
        self.key_right=lol[2]
        self.key_down=lol[3]
        self.key_mom=lol[4]

        
    
    def update(self):
        if keys[self.key_left]:
            self.rect.x-=self.speed_move
            self.direct=0
        elif keys[self.key_up]:
            self.rect.y-=self.speed_move
            self.direct=1
        elif keys[self.key_right]:
            self.rect.x+=self.speed_move
            self.direct=2
        elif keys[self.key_down]:
            self.rect.y+=self.speed_move
            self.direct=3
        if keys[self.key_mom] and self.count==self.dayn:
            speed_pylx = directs[self.direct][0] * self.speed_pyl
            speed_pyly = directs[self.direct][1] * self.speed_pyl
            Bullet(self, self.rect.centerx, self.rect.centery, speed_pylx, speed_pyly, self.damage_pyl)
            self.count=0
        if self.count<self.dayn:
            self.count+=1


        

        
        

    def draw(self):
        pygame.draw.rect(window,self.color,self.rect)
        x=self.rect.centerx+directs[self.direct][0]*15
        y=self.rect.centery+directs[self.direct][1]*15
        pygame.draw.line(window,'white',(self.rect.centerx,self.rect.centery),(x,y),3)
    def damage_pl(self, damage):
        self.helf -= damage
        if self.helf <= 0:
            objects.remove(self)

class Bullet:
    def __init__(self, strel, x, y, speed_pylx, speed_pyly, damage):
        pyls.append(self)
        self.strel = strel
        self.x = x
        self.y = y
        self.speed_pylx = speed_pylx
        self.speed_pyly = speed_pyly
        self.damage = damage

    def update(self):
        self.x += self.speed_pylx
        self.y += self.speed_pyly

        if self.x < 0 or self.y > width or self.y < 0 or self.y > vis:
            pyls.remove(self)
        else:
            for object in objects:
                if object != self.strel and object.rect.collidepoint(self.x, self.y):
                    object.damage_pl(self.damage)
                    pyls.remove(self)#
                    break





    def draw(self):
        pygame.draw.circle(window, 'pink', (self.x, self.y), 2)

class Block:
    def __init__(self, x, y, size):
        objects.append(self)
        self.type = 'block'
        self.rect = pygame.Rect(x, y, size, size)
        self.helf = 1

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(window, 'pink', self.rect)
        pygame.draw.rect(window, 'red', self.rect, 2)

    def damage_pl(self, damage):
        self.helf -= damage
        if self.helf <= 0:
            objects.remove(self)


pyls= []

objects=[]
Tank("green",50,50,0,[pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_r])
Tank('pink', 250, 350, 0, [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_l])
for i in range(70):#
    while True:#
        x = randint(0, width // tanker - 1) * tanker
        y = randint(0, width // tanker - 1) * tanker#
        lolk = pygame.Rect(x, y, tanker, tanker)
        found = False
        for object in objects:
            if lolk.colliderect(object.rect):
                found = True
       
        if found == False:
            break

    Block(x, y, tanker)#

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys=pygame.key.get_pressed()
    for object in objects:
        object.update()
    for pyl in pyls:
        pyl.update()
    
    window.fill("black")
    for pyl in pyls:
        pyl.draw()

    for object in objects:
        object.draw()
     


   
    pygame.display.update()
    clock.tick(fps)
