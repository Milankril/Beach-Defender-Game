import pygame


pygame.init()

screen = pygame.display.set_mode((520, 676)) # Background position

pygame.display.set_caption("Beach Defender")

bg = pygame.image.load('bg.png') # Background Image

clock = pygame.time.Clock()

green = (0,200,0)
red = (200,0,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

def button():
     mouse = pygame.mouse.get_pos()

     if 100+125 > mouse [0] > 100 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, green, (100,478,125,50))
     else:
        pygame.draw.rect(screen, bright_green, (100,478,125,50))
     play = font.render('PLAY', 1, ((0, 0, 0)))
     screen.blit(play, (100, 485))



     if 300+125 > mouse [0] > 300 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, red, (300,478,125,50))
     else:
        pygame.draw.rect(screen, bright_red, (300,478,125,50))
     Quit = font.render('QUIT', 1, ((0, 0, 0)))
     screen.blit(Quit, (300, 485))

def redrawGameWindow():
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))


    mouse = pygame.mouse.get_pos()

    if 100+125 > mouse [0] > 100 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, green, (100,478,125,50))
    else:
        pygame.draw.rect(screen, bright_green, (100,478,125,50))
    play = font.render('PLAY', 1, ((0, 0, 0)))
    screen.blit(play, (100, 485))



    if 300+125 >  mouse [0] > 300 and 478+50 > mouse [1] > 478:
        pygame.draw.rect(screen, red, (300,478,125,50))
    else:
        pygame.draw.rect(screen, bright_red, (300,478,125,50))
    Quit = font.render('QUIT', 1, ((0, 0, 0)))
    screen.blit(Quit, (300, 485))




    pygame.display.update()

font = pygame.font.SysFont('', 60, True)
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()


pygame.quit()




