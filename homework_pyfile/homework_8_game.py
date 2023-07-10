import pygame, sys, random
SCREEN_W, SCREEN_H = 800, 600 #set window size

class CLS_box(object): 
    def __init__(self, rect, speed, color = (255,255,255)):
        self.rect = pygame.Rect(rect)
        self.speed = speed
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

def create_box(rectList): #generate box randomly
    while True:
        x = random.randint(0, SCREEN_W)
        y = random.randint(0, SCREEN_H)
        w = random.randint(10, 40)
        h = random.randint(10, 40)
        rect = pygame.Rect(x, y, w, h)
        if (not rect.colliderect(homeBox)) and (rect.collidelist(rectList) == -1):
            break
    while True:
        speed = [random.randint(0,2) - 1, random.randint(0,2) - 1]
        if speed != [0, 0]:
            break
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return CLS_box(rect, speed, color)

#----pygame initialize----
pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption('RT Space')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

#----coding initialize----
homeBox = [300, 200, 200, 200]
myBox = CLS_box([380, 280, 10, 10], [0, 0], (0, 255, 0))
boxNumber = 100 #number of boxes
boxList, rectList = [], []
for i in range(boxNumber):
    b = create_box(rectList)
    boxList.append(b)
    rectList.append(b.rect)
timeStart = pygame.time.get_ticks()

#----main----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                myBox.speed[0] = -1
            if event.key == pygame.K_RIGHT:
                myBox.speed[0] = 1
            if event.key == pygame.K_UP:
                myBox.speed[1] = -1
            if event.key == pygame.K_DOWN:
                myBox.speed[1] = 1
    
    screen.fill((0, 0, 0))
    myBox.move()
    myBox.draw(screen)
    for b in boxList:
        if b.rect.x > SCREEN_W - b.rect.width or b.rect.x == 0:
            b.speed[0] = -b.speed[0]
        if b.rect.y > SCREEN_H - b.rect.height or b.rect.y == 0:
            b.speed[1] = -b.speed[1]
        for b0 in boxList:
            if b == b0:
                continue
            #----contact detection----
            if (abs(b0.rect.bottom - b.rect.top) <= 1) and (b.rect.right >= b0.rect.left) and (b0.rect.right >= b.rect.left):
                b.speed[1] = -b.speed[1]
            if (abs(b0.rect.top - b.rect.bottom) <= 1) and (b.rect.right >= b0.rect.left) and (b0.rect.right >= b.rect.left):
                b.speed[1] = -b.speed[1]
            if (abs(b0.rect.bottom - b.rect.top) <= 1) and (b.rect.right >= b0.rect.left) and (b0.rect.right >= b.rect.left):
                b.speed[1] = -b.speed[1]
            if (abs(b0.rect.bottom - b.rect.top) <= 1) and (b.rect.right >= b0.rect.left) and (b0.rect.right >= b.rect.left):
                b.speed[1] = -b.speed[1]
        b.move()
        b.draw(screen)
        if myBox.rect.colliderect(b.rect):
            print('score: ' + str((pygame.time.get_ticks() - timeStart) / 1000))
            pygame.quit()
            sys.exit()
    imgText = font.render(str((pygame.time.get_ticks() - timeStart) / 1000), True, (0, 0, 255))     
    screen.blit(imgText, (SCREEN_W - 100, 0))  
    pygame.display.update()
    clock.tick(50) 

