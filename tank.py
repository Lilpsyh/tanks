import pygame
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

        

        
        

    def draw(self):
        pygame.draw.rect(window,self.color,self.rect)
        x=self.rect.centerx+directs[self.direct][0]*15
        y=self.rect.centery+directs[self.direct][1]*15
        pygame.draw.line(window,'white',(self.rect.centerx,self.rect.centery),(x,y),3)


        

    
objects=[]
Tank("green",50,50,0,[pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_r])
Tank('pink', 250, 350, 0, [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_l])

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys=pygame.key.get_pressed()
    for object in objects:
        object.update()
    
    window.fill("black")
    for object in objects:
        object.draw()

   
    pygame.display.update()
    clock.tick(fps)


