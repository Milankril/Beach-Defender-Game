import pygame


pygame.init()

screenwidth = 520
screenheight = 676

screen = pygame.display.set_mode((screenwidth, screenheight)) # Background position

pygame.display.set_caption("Beach Defender")

bg = pygame.image.load('bg.png') # Background Image
br = pygame.image.load('br.png') # Background when playing game
x = (screenwidth*0.45)
y = (screenheight*0.8)

clock = pygame.time.Clock()

green = (0,200,0)
red = (200,0,0)
play = ''


bright_red = (255,0,0)
bright_green = (0,255,0)

def button(action=''):
    global scrn, play, run
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100+125 > mouse [0] > 100 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, green, (100,478,125,50))
        if click[0] == 1 and action == 'clicked':
            print("cancan")
            scrn = 1
            print(scrn)

    elif scrn == 0:
        pygame.draw.rect(screen, bright_green, (100,478,125,50))
    play = font.render('PLAY', 1, ((0, 0, 0)))
    screen.blit(play, (100, 485))


    if 300+125 > mouse [0] > 300 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, red, (300,478,125,50))
        if click[0] == 1 and action == 'pressed':
            run = False
    elif scrn == 0:
        pygame.draw.rect(screen, bright_red, (300,478,125,50))
    Quit = font.render('QUIT', 1, ((0, 0, 0)))
    screen.blit(Quit, (300, 485))

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


    if scrn == 1:
        screen.fill((255, 100, 100))
        screen.blit(br, (0, 0))

        mouse = pygame.mouse.get_pos()


        if 10+90 > mouse [0] > 10 and 10+25 > mouse [1] > 10:
            pygame.draw.rect(screen, green, (10,10,90,25))
        else:
            pygame.draw.rect(screen, bright_green, (10,10,90,25))
        play = fontB.render('BACK', 1, ((0, 0, 0)))
        screen.blit(play, (10, 10))


        pygame.display.update()



font = pygame.font.SysFont('', 60, True)
fontB = pygame.font.SysFont('', 40, True)
scrn = 0
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()


pygame.quit()




