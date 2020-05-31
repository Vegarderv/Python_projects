import pygame
import math

inventory = {}
a_last = [195,195,195]
gate_opening = [0,0,0]
spin = 0

pygame.init()

display_width = 1200
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (150, 0, 0)
dark_white = (200, 200, 200)
block_color = (0, 162, 232)
green = (31, 181, 4)
gold = (159, 138, 66)
table = [0,0,0,0,0,0,0,0,0,0,0,0]

bokImg = pygame.image.load('bok.png')
bokImg = pygame.transform.scale(bokImg, (300, 550))
propImg = pygame.image.load('prop.png')
bryterImg = pygame.image.load('Bryter_bak.png')
bryter_bakImg = pygame.image.load('Bryter_bak_bak.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OverRun')
clock = pygame.time.Clock()

clicked = pygame.mouse.get_pressed()

def ardu_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, size, x, y):
    largeText = pygame.font.SysFont('comicsansms', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,width,height,inactive,active, action=None):
    global click
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active, (x, y, width, height))
        if click == 1 and action != None:
            global next
            next=action
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, width, height))
    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x + (width / 2), y + (height / 2))
    gameDisplay.blit(textSurf, textRect)

def circle_button(msg,x,y,radius,inactive,active, action=None):
    global click
    mouse = pygame.mouse.get_pos()

    sqx = (mouse[0] - x)**2
    sqy = (mouse[1] - y)**2

    if math.sqrt(sqx + sqy) < radius:
        pygame.draw.circle(gameDisplay,active,(x,y),radius)
        if click == 1 and action != None:
            global next
            next=action
    else:
        pygame.draw.circle(gameDisplay, inactive, (x,y), radius)
    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x,y)
    gameDisplay.blit(textSurf, textRect)

def slider(x_place,y_place,width,height,key):
    global click
    pos = pygame.mouse.get_pos()

    correction = height / 8

    if click == 1 and x_place + width > pos[0] > x_place and y_place + height > pos[1] - correction > y_place:
        a = ((pos[1] - correction)- y_place) - 5
        if a < 0:
            a = 0
        elif a > x_place + height + correction:
            a = height - 10
        a_last[key] = a
    elif click == 1 and x_place + width > pos[0] > x_place and y_place + height + correction> pos[1] - correction> y_place + height:
        a = height - 5
        a_last[key] = a
    else:
        a = a_last[key]

    #pygame.draw.rect(gameDisplay, black, pygame.Rect(x_place, y_place, width, height))
    #pygame.draw.rect(gameDisplay, red, pygame.Rect(5 + x_place, a + y_place, width - 10, 5))

    bryter_bakImg_1 = pygame.transform.scale(bryter_bakImg, (width, height))
    gameDisplay.blit(bryter_bakImg_1, (x_place, y_place + correction))

    bryterImg_1 = pygame.transform.scale(bryterImg, (width - 10, 50))
    gameDisplay.blit(bryterImg_1, (5 + x_place, a + y_place))

    return ardu_map(a,0,height - 5,100,0)

def game_intro():
    message_display("OverRun", 100, 600, 100)

    message_display('"Kan du klare å styre et vassdrag å produsere nok energi for å redde verden?"', 20, 600, 200)

    message_display('"Prøv å styre dammene på vassdraget slik at det verkren går tørt eller blir oversvømelse. "', 20, 600, 260)
    message_display('"Du tjener penger på å selge strøm og kan forbedre turbinene. Kan du reddet miljøet og ungå klimasvinginger? "', 20,600, 290)

    knapp1 = button('Spill', 300, 700, 200, 50, dark_white, gold, game_loop)
    knapp2 = button('Leaderboard', 600, 700, 200, 50, dark_white, gold)

def game_loop():
    global spin

    gate_opening[0] = slider(200,500,50,200,0)
    gate_opening[1] = slider(400,500,50,200,1)
    gate_opening[2] = slider(600,500,50,200,2)

    if spin > 359:
        spin -= 360
    else:
        spin += (gate_opening[0] / 4)

    prop_Img = pygame.transform.rotate(propImg, spin)
    gameDisplay.blit(prop_Img, (100, 100))

    message_display('Turbin 1 går på {} %'.format(round(gate_opening[0],0)), 20, 600, 100)
    message_display('Turbin 2 går på {} %'.format(round(gate_opening[1],0)), 20, 600, 130)
    message_display('Turbin 3 går på {} %'.format(round(gate_opening[2],0)), 20, 600, 160)

    circle_button('Hei',1000,400,70,red,dark_red,game_intro)

next = game_intro

while True:
    knapp = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    click_prev = clicked[0]
    clicked = pygame.mouse.get_pressed()
    click=clicked[0]-click_prev

    next()

    pygame.display.update()
    gameDisplay.fill(white)