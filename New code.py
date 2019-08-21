import pygame
import random
pygame.init()
screenwidth = 520
screenheight = 676
screen = pygame.display.set_mode((screenwidth, screenheight)) # Background position
pygame.display.set_caption("Beach Defender")
bg = pygame.image.load('bg.png') # Background Image
br = pygame.image.load('br.png') # Background when playing game
clock = pygame.time.Clock()
green = (0,200,0)
red = (200,0,0)
play = ''
bright_red = (255,0,0)
bright_green = (0,255,0)
# xtrash = random.randint(20,460)
font = pygame.font.SysFont('', 60, True)
fontb = pygame.font.SysFont('', 40, True)
scrn = 0
score = 0
trashImg = pygame.image.load('trash.png')
binImg = pygame.image.load('bin.png')
lifeHeart = pygame.image.load('lifeHeart.png')
lifeHeart2 =pygame.image.load('lifeHeart.png')
lifeHeart3 = pygame.image.load('lifeHeart.png')
lifeHeart2size = pygame.transform.scale(lifeHeart, (30,30))
lifeHeart3size =pygame.transform.scale(lifeHeart, (30,30))
lifeHeartsize = pygame.transform.scale(lifeHeart, (30,30))
trashsize = pygame.transform.scale(trashImg, (50,50))
binsize = pygame.transform.scale(binImg, (100,100))



class bin(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.hitbox = (self.x,self.y, 97,30)

    def drawbin(self, screen):
        self.hitbox = (self.x,self.y, 97,30)
        screen.blit(binsize, (self.x, self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox,2)

    def movebin(self, screen):
        if keys[pygame.K_LEFT] and scrn == 1 and self.x > 5:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and scrn == 1 and self.x < 420:
            self.x += self.vel

    def hit(self):
        print('hit')






class falling_trash(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = (self.x, self.y, 50, 50)
    def draw(self, screen):
        self.hitbox = (self.x, self.y, 50, 50)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox,2)
        screen.blit(trashsize, (self.x, self.y))

def button(action=''):
    global scrn, play, run
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100+125 > mouse [0] > 100 and 478+50 > mouse [1] > 478 and scrn == 0:
        pygame.draw.rect(screen, green, (100,478,125,50))
        play = font.render('PLAY', 1, ((0, 0, 0)))
        screen.blit(play, (100, 485))
        if click[0] == 1 and action == 'clicked':
            print("cancan")
            scrn = 1
            print(scrn)
    elif scrn == 0:
        pygame.draw.rect(screen, bright_green, (100,478,125,50))
        play = font.render('PLAY', 1, ((0, 0, 0)))
        screen.blit(play, (100, 485))




    if 300+125 > mouse [0] > 300 and 478+50 > mouse [1] > 478 and scrn == 0:
        pygame.draw.rect(screen, red, (300,478,125,50))
        Quit = font.render('QUIT', 1, ((0, 0, 0)))
        screen.blit(Quit, (300, 485))
        if click[0] == 1 and action == 'pressed':
            run = False
    elif scrn == 0:
        pygame.draw.rect(screen, bright_red, (300,478,125,50))
        Quit = font.render('QUIT', 1, ((0, 0, 0)))
        screen.blit(Quit, (300, 485))


    if 10+90 > mouse [0] > 10 and 10+25 > mouse [1] > 10 and scrn == 1:
        pygame.draw.rect(screen, green, (10,10,90,25))
        back = fontb.render('BACK', 1, ((0, 0, 0)))
        screen.blit(back, (10, 10))
        if click[0] == 1 and action == 'pushed':
            print("cancan")
            scrn = 0
            print(scrn)
    elif scrn == 1:
        pygame.draw.rect(screen, bright_green, (10,10,90,25))
        back = fontb.render('BACK', 1, ((0, 0, 0)))
        screen.blit(back, (10, 10))


def redrawGameWindow():
    global scrn
    screen.fill((255, 255, 255))
    if scrn == 0:
        screen.blit(bg, (0, 0))
        mouse = pygame.mouse.get_pos()
        '''
        if 100+125 > mouse [0] > 100 and 478+50 > mouse [1] > 478:
            pygame.draw.rect(screen, green, (100,478,125,50))
        else:
            pygame.draw.rect(screen, bright_green, (100,478,125,50))
        play = font.render('PLAY', 1, ((0, 0, 0)))
        screen.blit(play, (100, 485))
        '''
        button('clicked')
        '''
        if 300+125 >  mouse [0] > 300 and 478+50 > mouse [1] > 478:
            pygame.draw.rect(screen, red, (300,478,125,50))
        else:
            pygame.draw.rect(screen, bright_red, (300,478,125,50))
        Quit = font.render('QUIT', 1, ((0, 0, 0)))
        screen.blit(Quit, (300, 485))
        '''
        button('pressed')


        pygame.display.update()


    if scrn==1:
        screen.blit(br, (0, 0))
        if life == 3:
            screen.blit(lifeHeartsize, (390,10))
            screen.blit(lifeHeart2size, (420,10))
            screen.blit(lifeHeart3size, (450,10))
        if life == 2:
            screen.blit(lifeHeartsize, (390,10))
            screen.blit(lifeHeart2size, (420,10))
        if life == 1:
            screen.blit(lifeHeartsize, (390,10))
        if life == 0:
            scrn = 2
        mouse = pygame.mouse.get_pos()

        '''
        if 10+90 > mouse [0] > 10 and 10+25 > mouse [1] > 10:
        pygame.draw.rect(screen, green, (10,10,90,25))
        else:
        pygame.draw.rect(screen, bright_green, (10,10,90,25))
        back = fontb.render('BACK', 1, ((0, 0, 0)))
        screen.blit(back, (10, 10))
        '''
        button('pushed')


        text = fontc.render('SCORE: ' + str(score), 1, (0,0,0))
        screen.blit(text, (170,10))
        for falling_trash1 in fallingrubbish:
            falling_trash1.draw(screen)
        bin1.drawbin(screen)
        pygame.display.update()

    if scrn == 2:
        screen.fill((0, 0, 0))
        end = fontd.render("END, THE BEACH WAS POLLUTED", 1, (255, 255, 255))
        screen.blit(end, (50, 300))
        pygame.display.update()




fontc = pygame.font.SysFont('comicsans',40,True)
fontd = pygame.font.SysFont('comicsans',30,True)
x = 260
y = 550

x_change = 0

# falling_trash1 = falling_trash(xtrash, 50, 50, 50)
bin1 = bin(260, 550, 100, 100)


fallingrubbish = []
rand_x = 0
falling = False
falling_wait = 0
random_time = 0

life = 3

run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for falling_trash1 in fallingrubbish:
        if scrn == 1:
            if falling_trash1.y < 0:
                falling_trash1.y = 0
            elif falling_trash1.y < 600:
                falling_trash1.y += 5
            falling_trash1.width = 50
            falling_trash1.height = 50
            if falling_trash1.y - 50 < bin1.hitbox[1] + bin1.hitbox[3] and falling_trash1.y + 50 > bin1.hitbox[1]:
                if falling_trash1.x + 50 > bin1.hitbox[0] and falling_trash1.x < bin1.hitbox[0] + bin1.hitbox[2]:
                    bin1.hit()
                    score += 1
                    fallingrubbish.pop(fallingrubbish.index(falling_trash1))

            if falling_trash1.y > 599:
                life -= 1
                fallingrubbish.pop(fallingrubbish.index(falling_trash1))

    if scrn == 1 and not falling:
        falling = True
        random_time = random.randint(16, 80)
        if len(fallingrubbish) < 4:
            rand_x = random.randint(0, 520 - bin1.width)
            fallingrubbish.append(falling_trash(rand_x, 0, 50, 50))



    if falling:
        falling_wait += 1
    if falling_wait == random_time:
        falling = False
        falling_wait = 0

    keys = pygame.key.get_pressed()







    if keys[pygame.K_LEFT] and scrn == 1 and bin1.x > 5:
        bin1.x -= bin1.vel
    if keys[pygame.K_RIGHT] and scrn == 1 and bin1.x < 420:
        bin1.x += bin1.vel






    clock.tick(80)

    redrawGameWindow()

pygame.quit()
