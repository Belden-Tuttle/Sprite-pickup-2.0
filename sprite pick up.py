import pygame
import random
 

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
class Player(pygame.sprite.Sprite):
     
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

 
class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(-1,2,2)
        self.change_y = random.randrange(-1,2,2)
        self.left_boundary = 0
        self.right_boundary = 700
        self.top_boundary = 0
        self.bottom_boundary = 500

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary:
            self.change_x = random.randrange(-3,0)
        if self.rect.left <= self.left_boundary:
            self.change_x = random.randrange(1,4)
        if self.rect.bottom >= self.bottom_boundary:
            self.change_y = random.randrange(-3,0)
        if self.rect.top <= self.top_boundary:
            self.change_y = random.randrange(1,4)
                


class Bad_block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.change_x = random.randrange(-3,4)
        self.change_y = random.randrange(-3,4)
        self.left_boundary = 0
        self.right_boundary = 700
        self.top_boundary = 0
        self.bottom_boundary = 500

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary:
            self.change_x = random.randrange(-1,0)
        if self.rect.left <= self.left_boundary:
            self.change_x = random.randrange(1,2)
        if self.rect.bottom >= self.bottom_boundary:
            self.change_y = random.randrange(-1,0)
        if self.rect.top <= self.top_boundary:
            self.change_y = random.randrange(1,2)

 

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255) 
 
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
 
pygame.display.set_caption("Block game")

block_list = pygame.sprite.Group()
bb_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(25):
    block = Block(BLACK, 20, 20)
    block.rect.x = random.randrange(screen_width-20)
    block.rect.y = random.randrange(screen_height-20)
    block_list.add(block)
    all_sprites_list.add(block)


for i in range(25):
    block = Bad_block(RED, 20, 20)
    block.rect.x = random.randrange(screen_width-20)
    block.rect.y = random.randrange(screen_height-20)
    bb_list.add(block)
    all_sprites_list.add(block)

 

 
player = Player(GREEN ,20, 20)
player.rect.x = 350
player.rect.y = 250
all_sprites_list.add(player)
 

done = False
change_x = 0
change_y = 0
good_sound = pygame.mixer.Sound("laser1.wav")
bad_sound = pygame.mixer.Sound("laser2.wav")
clock = pygame.time.Clock()
score = 0
end = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = (-3)
                
            if event.key == pygame.K_RIGHT:
                change_x = (3)
                
            if event.key == pygame.K_UP:
                change_y = (-3)
                
            if event.key == pygame.K_DOWN:
                change_y = (3)
                
                
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
                change_x = 0
                
            if event.key == pygame.K_RIGHT:
                change_x = 0

            if event.key == pygame.K_UP:
                change_y = 0

            if event.key == pygame.K_DOWN:
                change_y = 0



    if len(block_list) == 0:
            end = True

    player.rect.x += change_x
    player.rect.y += change_y

    if player.rect.x >= 680:
            player.rect.x = 680

    if player.rect.x <= 0:
            player.rect.x = 0

    if player.rect.y >= 480:
            player.rect.y = 480

    if player.rect.y <= 0:
            player.rect.y = 0

    for i in block_list:
        i.move()

    
    for i in bb_list:
        i.move()

   

    
   
    screen.fill(WHITE)
 
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    bb_hit_list = pygame.sprite.spritecollide(player, bb_list, True)

    for block in blocks_hit_list:
        good_sound.play()
        score += 1
        print(score)

    for bb in bb_hit_list:
        bad_sound.play()
        score -=1
        print(score)
 

    all_sprites_list.draw(screen)

    
    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(str(score), True, GREEN)

    screen.blit(text, [0,0])

    

    if end == True:

        screen.fill (BLACK)

        font = pygame.font.SysFont('Calibri', 25, True, False)

        text = font.render(str(score), True, GREEN)

        screen.blit(text, [250,250])

        done = True
    
 
    pygame.display.flip()
 
    clock.tick(60)

    
 
pygame.quit()

