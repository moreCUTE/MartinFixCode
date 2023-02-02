# Martin Rivera A debugged this

import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500)) #to set a display you need double parentheses
pygame.display.set_caption("Breakoiut")

px = 320
py = 470

bx = 350
by = 465
bVx = 5
bVy = 5

lives = 3
score = 0
class Boop:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    def draw(self):
        if self.alive is True:
            pygame.draw.rect(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), (self.xpos, self.ypos, 50, 20), 10) #its random instead of rando
    def collide(self, x, y):
        if self.alive is True:
            if x+20 > self.xpos and x<self.xpos+50 and y+20 > self.ypos and y < self.ypos+20:
                self.alive = False
                return True

doExit = False
clock = pygame.time.Clock()

b1 = Boop(20,20)
b2 = Boop(80, 20)
b3 = Boop(140, 20)
b4 = Boop(200, 20)
b5 = Boop(260, 20)
b6 = Boop(320,20)
b7 = Boop(380, 20)
b8 = Boop(440, 20)
b9 = Boop(500, 20)
b10 = Boop(560, 20)
b11 = Boop (620, 20)
b12 = Boop(20,45)
b13 = Boop(80, 45)
b14 = Boop(140, 45)
b15 = Boop(200, 45)
b16 = Boop(260, 45)
b17 = Boop(320,45)
b18 = Boop(380, 45)
b19 = Boop(440, 45)
b20 = Boop(500, 45)
b21 = Boop(560, 45)
b22 = Boop (620, 45)
b23 = Boop(20,70)
b24 = Boop(80, 70)
b25 = Boop(140, 70)
b26 = Boop(200, 70)
b27 = Boop(260, 70)
b28 = Boop(320, 70)
b29 = Boop(380, 70)
b30 = Boop(440, 70)
b31 = Boop(500, 70)
b32 = Boop(560, 70)
b33 = Boop (620, 70)
while not doExit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        px -= 7
    if keys[pygame.K_RIGHT]:
        px+=7

    
    bx += bVx
    by += bVy
    
    if bx < 0 or bx + 20 > 700:
        bVx *= -1 
    if by < 0:
        bVy *= -1
        
    if b1.collide(bx, by):
        bVy *=-1
        score += 100
    if b2.collide(bx, by):
        bVy *=-1
        score += 100
    if b3.collide(bx, by):
        bVy *=-1
        score += 100
    if b4.collide(bx, by):
        bVy *=-1
        score += 100
    if b5.collide(bx, by):
        bVy *=-1
        score += 100
    if b6.collide(bx, by):
        bVy *=-1
        score += 100
    if b7.collide(bx, by):
        bVy *=-1
        score += 100
    if b8.collide(bx, by):
        bVy *=-1
        score += 100
    if b9.collide(bx, by):
        bVy *=-1
        score += 100
    if b10.collide(bx, by):
        bVy *=-1
        score += 100
    if b11.collide(bx, by):
        bVy *=-1
        score += 100
    if b12.collide(bx, by):
        bVy *=-1
        score += 100
    if b13.collide(bx, by):
        bVy *=-1
        score += 100
    if b14.collide(bx, by):
        bVy *=-1
        score += 100
    if b15.collide(bx, by):
        bVy *=-1
        score += 100
    if b16.collide(bx, by):
        bVy *=-1
        score += 100
    if b17.collide(bx, by):
        bVy *=-1
        score += 100
    if b18.collide(bx, by):
        bVy *=-1
        score += 100
    if b19.collide(bx, by):
        bVy *=-1
        score += 100
    if b20.collide(bx, by):
        bVy *=-1
        score += 100
    if b21.collide(bx, by):
        bVy *=-1
        score += 100
    if b22.collide(bx, by):
        bVy *=-1
        score += 100
    if b23.collide(bx, by):
        bVy *=-1
        score += 100
    if b24.collide(bx, by):
        bVy *=-1
        score += 100
    if b25.collide(bx, by):
        bVy *=-1
        score += 100
    if b26.collide(bx, by):
        bVy *=-1
        score += 100
    if b27.collide(bx, by):
        bVy *=-1
        score += 100
    if b28.collide(bx, by):
        bVy *=-1
        score += 100
    if b29.collide(bx, by):
        bVy *=-1
        score += 100
    if b30.collide(bx, by):
        bVy *=-1
        score += 100
    if b31.collide(bx, by):
        bVy *=-1
        score += 100
    if b32.collide(bx, by):
        bVy *=-1
        score += 100
    if b33.collide(bx, by):
        bVy *=-1
        score += 100
    #paddle/ball collision
    if bx < px + 100 and bx > px and by  > py and by < py + 20:
        bVy *= -1
    #ground collision
    if by >= 500:
        lives -= 1
        bx = 350
        by = 250 

#Drawing Boops
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    #screen fill also helps so the screen doesn't fill yp with one color

    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()
    b13.draw()
    b14.draw()
    b15.draw()
    b16.draw()
    b17.draw()
    b18.draw()
    b19.draw()
    b20.draw()
    b21.draw()
    b22.draw()
    b23.draw()
    b24.draw()
    b25.draw()
    b26.draw()
    b27.draw()
    b28.draw()
    b29.draw()
    b30.draw()
    b31.draw()
    b32.draw()
    
    font = pygame.font.Font(None, 15)
    text = font.render(str(lives),1, (0, 255, 0))
    screen.blit(text, (660, 9))
    font = pygame.font.Font(None, 15)
    text = font.render(str(score),1, (0, 255, 0))
    screen.blit(text, (40, 9))
    
    pygame.draw.rect(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), (px, py, 100, 20), 10)
    pygame.draw.circle(screen, (218, 71, 255), (bx, by), 6)
    pygame.display.flip()
pygame.quit()
