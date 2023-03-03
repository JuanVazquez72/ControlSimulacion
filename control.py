import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 389,187
screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load("prueba.png").convert()
frameRect = pygame.Rect((0,0), (width,height))

crosshair = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshair,pygame.Color("Red"), (5,5), 5,0)

crosshairb = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshairb,pygame.Color("blue"), (5,5), 5,0)


while True:
    pygame.event.pump()
    screen.blit(background_image, (0,0))


    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_x]:screen.blit(crosshair, (289,110))
    
    if Keys[pygame.K_a]:screen.blit(crosshair, (255,85))

    if Keys[pygame.K_b]:screen.blit(crosshair, (287,32))

    if Keys[pygame.K_c]:screen.blit(crosshair, (166,95))

    if Keys[pygame.K_q]:screen.blit(crosshair, (87,32))

    if Keys[pygame.K_w]:screen.blit(crosshair, (283,65))

    if Keys[pygame.K_d]:screen.blit(crosshairb, (315,90))

    if Keys[pygame.K_r]:screen.blit(crosshair, (205,95))


    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(crosshair,((x*20)+96-5,(y*20)+94-5))
    pygame.display.flip()
    clk.tick(40)

     # x=joy.get_axis(0)
    #y=joy.get_axis(1)
    #screen.blit(crosshairb,((x*20)+114,(y*20)+135))
    
   # for b in range(joy.get_numbuttons()):
    #    if joy.get_button(b):
     #       screen.blit(buttons[b][0], buttons[b][1])
