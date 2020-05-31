import pygame
import math
import random
import time
import threading
import key_board_input

def value_set():
    global inventory, a_last, gate_opening, fps, tid, t_pause, nedbør_log, text_for_print, A_t1, A_t2, A_t3, h_1, h_2, h_3, g, q_inn1, q_inn2, q_inn3, C, k, t, dt, h_lim, t_lim, t_hist, h1_hist, h2_hist, h3_hist, dagsfaktor, random1, random2, random3, random4, ran1, dag, virkningsgrad_1, virkningsgrad_2, virkningsgrad_3, oppg_key_1, oppg_key_2, oppg_key_3, kapital, max_vann_1, max_vann_2, max_vann_3, min_vann_1, min_vann_2, min_vann_3, buffer_1, buffer_2, buffer_3, spinn, prop_scal, strømfaktor, vannfaktor, hidden_kapital

    inventory = {}
    a_last = [195,195,195]
    gate_opening = [0,0,0]
    #spin = 0
    fps = 15
    tid =1
    t_pause = 0
    nedbør_log = []
    text_for_print = []

    A_t1 = 20000.00
    A_t2 = 40000.00  # Tank 2 tverrsnittareal (m^2)
    A_t3 = 10000.00
    h_1 = 40 # Vannivået i tank 1 når forsøket starter (m)
    h_2 = 40 # Vannivået i tank 2 når forsøket starter (m)
    h_3 = 40
    g = 9.81 # Gravitasjonskonstanten (m/s^2)
    q_inn1 = 0.001 # Mengde vann inn i toppen av tanken (m^3/s)
    q_inn2 = 0 # initialverdi for innstrømming i tank 2
    q_inn3 = 0
    C = 0.61
    k = C * math.sqrt(2*g)
    t = 0  # starttiden
    dt = 60 # tidssteg i sekunder
    h_lim = 0.01 # vi stopper beregningen når høyden er mindre enn denne
    t_lim = 10000 # vi stopper beregningen etter 4800 sekunder
    t_hist = [] # Lagerplass for historiske tidspunkter
    h1_hist = [] # Lagerplass for historiske h-verdier
    h2_hist = [] # Lagerplass for historiske h-verdier
    h3_hist = []
    dagsfaktor = 100
    random1 = 0
    random2 = 0
    random3 = 0
    random4 = 0
    ran1 = False
    dag = 1
    virkningsgrad_1 = 0.05
    virkningsgrad_2 = 0.05
    virkningsgrad_3 = 0.05
    oppg_key_1 = 1
    oppg_key_2 = 1
    oppg_key_3 = 1
    kapital = 0
    hidden_kapital = 0
    min_vann_1 = 30
    min_vann_2 = 30
    min_vann_3 = 30
    max_vann_1 = 114
    max_vann_2 = 114
    max_vann_3 = 114
    buffer_1 = 5
    buffer_2 = 5
    buffer_3 = 5
    spinn = [0,0,0]
    prop_scal = 26

    strømfaktor = 60
    vannfaktor = 0

mute = False
value_set()

pygame.init()

display_width = 1200
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (150, 0, 0)
dark_white = (200, 200, 200)
dark_blue = (0,0,150)
block_color = (0, 162, 232)
green = (31, 181, 4)
gold = (159, 138, 66)
table = [0,0,0,0,0,0,0,0,0,0,0,0]

bokImg = pygame.image.load('bok.png')
bokImg = pygame.transform.scale(bokImg, (300, 550))
propImg = pygame.image.load('propell_2.png')
propImg = pygame.transform.scale(propImg, (prop_scal,prop_scal))
bryterImg = pygame.image.load('Bryter_bak_2.png')
bryter_bakImg = pygame.image.load('Bryter_bak_bak_2.png')
controlImg = pygame.image.load('Controll.jpg')
controlImg = pygame.transform.scale(controlImg,(516,300))
ac_pauImg = pygame.image.load('Pause_active.png')
in_pauImg = pygame.image.load('Pause_inactive.png')
backgroundImg = pygame.image.load('background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg,(display_width,display_height))
damImg = pygame.image.load('dam.png')
damImg = pygame.transform.scale(damImg,(240,145))
kalenderImg = pygame.image.load('kalender.png')
kalenderImg = pygame.transform.scale(kalenderImg,(200,240))
solImg = pygame.image.load('sol.png')
solImg = pygame.transform.scale(solImg,(130,130))
sol_skyImg = pygame.image.load('sol_sky.png')
sol_skyImg = pygame.transform.scale(sol_skyImg,(130,130))
sol_sky_regnImg = pygame.image.load('sol_sky_regn.png')
sol_sky_regnImg = pygame.transform.scale(sol_sky_regnImg,(130,130))
sang = pygame.mixer.music.load("Sang.mp3")
muteImg = pygame.image.load('mute.png')
nonmuteImg = pygame.image.load('nonmute.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OverRun')
clock = pygame.time.Clock()
Icon = pygame.image.load('Welle.png')
pygame.display.set_icon(Icon)
clicked = pygame.mouse.get_pressed()


#Div. events som kan kjøres for å lage mer dynamisk spill
def MDG():
    global min_vann_1, min_vann_2, min_vann_3, max_vann_1, max_vann_2, max_vann_3, strømfaktor
    min_vann_1 += 5
    min_vann_2 += 5
    min_vann_3 += 5
    max_vann_1 -= 5
    max_vann_2 -= 5
    max_vann_3 -= 5
    strømfaktor += 20
    for i in range(100):
        message_display("MDG kommer til makta! Vannreguleringsnivået senkes, men strømprisen økes!", 20, 400, 400)
        message_display("OverRun", 30, 600, 60)
        button('Resume', 500, 350, 200, 50, dark_white, dark_blue, game_loop)
        pygame.rect.Rect(50,50,1100,700)
        clock.tick(fps)
        gameDisplay.fill(white)
def FrP():
    global min_vann_1, min_vann_2, min_vann_3, max_vann_1, max_vann_2, max_vann_3, strømfaktor
    min_vann_1 -= 5
    min_vann_2 -= 5
    min_vann_3 -= 5
    max_vann_1 += 5
    max_vann_2 += 5
    max_vann_3 += 5
    strømfaktor -= 20
    for i in range(100):
        message_display("FrP kommer til makta! Vannreguleringsnivået økes, men strømprisen senkes!", 20, 400, 400)
        message_display("OverRun", 30, 600, 60)
        button('Resume', 500, 350, 200, 50, dark_white, dark_blue, game_loop)
        pygame.rect.Rect(50,50,1100,700)
        clock.tick(fps)
        gameDisplay.fill(white)
def Saudi():
    global min_vann_1, min_vann_2, min_vann_3, max_vann_1, max_vann_2, max_vann_3, strømfaktor
    strømfaktor -= 20
    for i in range(100):
        message_display("Saudi arabia trapper opp oljepumpinga. Strømprisen senkes!", 20, 400, 400)
        message_display("OverRun", 30, 600, 60)
        button('Resume', 500, 350, 200, 50, dark_white, dark_blue, game_loop)
        pygame.rect.Rect(50, 50, 1100, 700)
        clock.tick(fps)
        gameDisplay.fill(white)
def nedbørr():
    global min_vann_1, min_vann_2, min_vann_3, max_vann_1, max_vann_2, max_vann_3, strømfaktor
    message_display("Det er meldt store mengder nedbør!", 20, 400, 400)
    vannfaktor += 20
    for i in range(100):
        message_display("Det er meldt store mengder nedbør!", 20, 400, 400)
        message_display("OverRun", 30, 600, 60)
        button('Resume', 500, 350, 200, 50, dark_white, dark_blue, game_loop)
        pygame.rect.Rect(50, 50, 1100, 700)
        clock.tick(fps)
        gameDisplay.fill(white)





def euler(h, dh, dt):
    '''Regner ut ny høyde i tanken vet tiden t+dt,
    gitt høyden og stigningstallet dh ved tiden t.'''
    return h + dh * dt

def stigning(A_h, A_t, h, q_inn):
    '''Regner ut stigningen i punktet h.
    Parameteren k er en global konstant.'''
    return 1/A_t * ((q_inn) - A_h * k * math.sqrt(h))

def hastighet(h):
    '''Regner ut hastigheten til væskestrømmen ut av tanken
    når væskehøyden er h. Parameteren k er en global konstant.'''
    if h > 0.0:
        return k * math.sqrt(h)
    else:
        return 0.0

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

def message_display_2(text, size, x, y,color=(0,0,0)):
    largeText = pygame.font.SysFont('comicsansms', size)
    l_Text = largeText.render(str(text),1,color)
    #TextSurf, TextRect = text_objects(text, l_Text)
    TextRect = (x, y)
    gameDisplay.blit(l_Text, TextRect)

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

def button_Img(x,y,width,height,inactive,active, action=None):
    global click
    mouse = pygame.mouse.get_pos()
    active = pygame.transform.scale(active, (width, height))
    inactive = pygame.transform.scale(inactive, (width, height))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        gameDisplay.blit(active,(x,y))
        if click == 1 and action != None:
            global next
            next=action
    else:
        gameDisplay.blit(inactive,(x,y))

def mute_button(x,y,width,height,inactive,active):
    global click
    global mute
    mouse = pygame.mouse.get_pos()
    active = pygame.transform.scale(active, (width, height))
    inactive = pygame.transform.scale(inactive, (width, height))
    active_1 = pygame.transform.scale(active, (width - 10, height - 10))
    inactive_1 = pygame.transform.scale(inactive, (width - 10, height - 10))
    if mute == False:
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(active_1,(x,y))
            if click == 1:
                mute = True
                pygame.mixer.music.set_volume(0.0)
        else:
            gameDisplay.blit(active,(x,y))
    elif mute == True:
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(inactive_1,(x,y))
            if click == 1:
                mute = False
                pygame.mixer.music.set_volume(1.0)
        else:
            gameDisplay.blit(inactive,(x,y))

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
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    correction = height / 8

    if pressed[0] == 1 and x_place + width > pos[0] > x_place and y_place + height > pos[1] - correction > y_place:
        a = ((pos[1] - correction)- y_place) - 5
        if a < 0:
            a = 0
        elif a > x_place + height + correction:
            a = height - 10
        a_last[key] = a
    elif pressed[0] == 1 and x_place + width > pos[0] > x_place and y_place + height + correction> pos[1] - correction> y_place + height:
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

def text_box(x_place,y_place,width,height,active,inactive,size=30):
    global text_for_print
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    action = False
    print_key = True
    x_place=x_place-width/2

    pygame.draw.rect(gameDisplay,white,(x_place,y_place,width,height))

    if x_place + width > pos[0] > x_place and y_place + height > pos[1] > y_place:
        if pressed[0] == 1 or action == True:
            action = True
            while print_key:
                text_two = key_board_input.key_board()
                if text_two != None and text_two != '-1':
                    text_for_print.append(text_two)
                if text_two == '-1' and len(text_for_print) > 0:
                    del(text_for_print[-1])
                print_key = key_board_input.key_key()
                fin_tex = ''.join(text_for_print)
                message_display_2(fin_tex, size, x_place + 10, y_place, black)
                pygame.draw.rect(gameDisplay, active, (x_place, y_place, width, height), 5)
                pygame.display.update(pygame.rect.Rect(x_place, y_place, width, height))
                gameDisplay.fill(white)
        else:
            pygame.draw.rect(gameDisplay,active,(x_place,y_place,width,height),3)
            action = False
    else:
        action = False
        pygame.draw.rect(gameDisplay, inactive, (x_place, y_place, width, height), 3)

    fin_tex = ''.join(text_for_print)
    message_display_2(fin_tex, size, x_place + 10, y_place, black)
    action = True
    key_board_input.key_key(True)

def vannstand(bredde, høyde, x, y, farge):
    pygame.draw.rect(gameDisplay, farge, (x, y - høyde, bredde, høyde))

def nedbør(dag):
    global vannfaktor
    vann = 0.05 * dag * math.sin((dag*math.pi)/91.25)+(dag*math.pi)/60 + vannfaktor
    vann = random.randrange(int(vann - 20),int(vann + 21))
    if vann < 0:
        vann = 0
    return vann

def dato(t):
    måned = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
    dag = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    år = int((t-1) / 365)
    if t > 365:
        t = (t - år*365)
    for i in range(12):
        if dag[i] < t <= dag[i+1]:
            m = måned[i]
            dagen = t - dag[i]
    return dagen,m,år + 2018

def strøm(q_ut, virkningsgrad, strømpris):
    strømmen = q_ut * virkningsgrad * strømpris
    if strømmen < 1:
        strømmen = 0
    strømmen = round(strømmen,0)
    return strømmen

def strømpris(dag):
    global strømfaktor
    return 50 * math.cos(((math.pi * dag)/182.5)-(math.pi/4)) + strømfaktor

def score():
    global dag, hidden_kapital
    return hidden_kapital / 100 + dag * 20

def moneynator(money):
    millions =int(money / 1000000)
    thousands = int((money - millions*1000000) / 1000)
    rest = int(money-millions*1000000-thousands*1000)
    if millions > 0:
        return str(millions) + ' ' + str(thousands) + ' ' + str(rest)
    elif thousands > 0:
        return str(thousands) + ' ' + str(rest)
    else:
        return str(rest)

def spin(gate_opp,key):
    spinn[key-1] += (gate_opp / 4)
    if spinn[key - 1] > 359:
        spinn[key - 1] -= 360

def spin_2(sp):
    global prop_scal
    spining = sp*math.pi/180
    while spining >= 0.5*math.pi:
        spining-=0.5*math.pi
    D = -(prop_scal/2) * (math.cos(spining) + math.sin(spining))
    return D

def oppgrader_1():
    global oppg_key_1
    global virkningsgrad_1
    global kapital
    global next

    opp = 10000 * (oppg_key_1 ** 5)
    virkningsgrad_1 += 0.05
    kapital -= opp
    oppg_key_1 += 1

    next = game_loop
    game_loop()

def oppgrader_2():
    global oppg_key_2
    global virkningsgrad_2
    global kapital
    global next

    opp = 10000 * (oppg_key_2 ** 5)
    virkningsgrad_2 += 0.05
    kapital -= opp
    oppg_key_2 += 1

    next = game_loop
    game_loop()

def oppgrader_3():
    global oppg_key_3
    global virkningsgrad_3
    global kapital
    global next

    opp = 10000 * (oppg_key_3 ** 5)
    virkningsgrad_3 += 0.05
    kapital -= opp
    oppg_key_3 += 1

    next = game_loop
    game_loop()

def game_intro():
    global text_for_print

    message_display("OverRun", 100, 600, 100)

    message_display('"Kan du klare å styre et vassdrag å produsere nok energi for å redde verden?"', 20, 600, 200)

    message_display('"Prøv å styre dammene på vassdraget slik at det verkren går tørt eller blir oversvømelse. "', 20, 600, 260)
    message_display('"Du tjener penger på å selge strøm og kan forbedre turbinene. Kan du reddet miljøet og ungå klimasvinginger? "', 20,600, 290)
    pygame.mixer.music.play(-1, 0.0)
    knapp1 = button('Spill', 300, 700, 200, 50, dark_white, gold, game_loop)
    knapp2 = button('Leaderboard', 600, 700, 200, 50, dark_white, gold,leaderboard_show)

    #setter gjellende navnfil
    #text_for_print = []

    value_set()

    if len(nedbør_log) < 6:
        for i in range(1,7):
            nedbør_log.append(nedbør(i))

def pause():
    global next, dag
    next = pause

    message_display("OverRun", 30, 600, 60)
    message_display('Pause',100,600,130)

    button('Resume',500,350,200,50,dark_white,dark_blue,game_loop)

    message_display(str(dato(dag)),15,600,250)

def Event():
    global next, dag
    print('Fuck')
    Pos_eve = [FrP,Saudi,MDG]
    pos_eve_cho = random.randrange(len(Pos_eve))
    next = Pos_eve[pos_eve_cho]
    next()

def game_over():
    global next
    next = game_over
    message_display('Innskjøen tørket ut',40,600,60)
    button('Forsett', 500, 700, 200, 50, dark_white, gold, leaderboard_up)

def game_over_high():
    global next
    next = game_over_high

    message_display('Demningen brast!',40,600,60)
    button('Forsett', 500, 700, 200, 50, dark_white, gold, leaderboard_up)

def leaderboard_up():
    global next
    next = leaderboard_up

    message_display('Din sluttsum:',40,600,60)
    message_display('{} poeng'.format(score()),20,600,120)
    message_display('Skriv ditt navn her:',20,600,200)
    text_box(600, 250, 300, 50, dark_blue, black,35)
    message_display("Trykk 'Enter' for å gå videre.",20,600,320)
    button('Forsett',500,700,200,50,dark_white,gold,leaderboard_fix)

def leaderboard_fix():
    global text_for_print, next
    next = leaderboard_show

    top_list = []

    def getKey(item):
        return item[1]

    # Leser av filen og lagrer som tupple
    with open('toplist', "r") as fp:
        for i in fp.readlines():
            tmp = i.split(',')
            try:
                top_list.append((str(tmp[0]), int(tmp[1])))
            except:pass

    # Legger til den aktuelle spilleren
    top_list.append((''.join(text_for_print) + '', int(score())))

    # Sorterer den i riktig rekkefølge etter verdi nummer 2 i tuppelen
    top_list = sorted(top_list, key=getKey, reverse=True)

    # Skriver den nye listen i tekstfilen med riktig oppsett slik at den kan leses som tupple igjen
    with open('toplist','w') as fp:
        for i in range(0, len(top_list), 1):
            fp.write('\n' + str(top_list[i][0]) + ',' + str(top_list[i][1]))
        fp.close()

def leaderboard_show():
    global next
    next = leaderboard_show

    top_list = []

    message_display('Toppliste',40,600,50)

    # Leser av filen og lagrer som tupple
    with open('toplist', "r") as fp:
        for i in fp.readlines():
            tmp = i.split(',')
            try:
                top_list.append((str(tmp[0]), int(tmp[1])))
            except:pass

    place = 0
    for item in top_list:
        message_display_2('{}    {}'.format(int(((place + 50) / 50)),item[0]),30,300,150 + place)
        message_display_2('{} poeng'.format(item[1]), 30, 800 - len(str(item[1])) * 17, 150 + place)
        place += 50

    button('Tilbake', 500, 700, 200, 50, dark_white, gold, game_intro)

def game_loop():
    global spin, tid, h_1, h_2, h_3, dagsfaktor, q_inn1, random1, random2, random3, random4, ran1, dag, kapital, oppg_key_1, oppg_key_2, oppg_key_3, virkningsgrad_1, virkningsgrad_2, virkningsgrad_3, min_vann_1, min_vann_2, min_vann_3, max_vann_1, max_vann_2, max_vann_3, buffer_1, buffer_2, buffer_3, next, hidden_kapital
    next = game_loop

    gameDisplay.blit(backgroundImg,(0,0))
    dagsfaktor += 1

    gate_opening[0] = slider(380,485,50,200,0)
    gate_opening[1] = slider(455,485,50,200,1)
    gate_opening[2] = slider(530,485,50,200,2)

    A_h1 = 0.02 * gate_opening[0] + 0.0000001  # Hull 1 tverrsnittareal (m^2)
    A_h2 = 0.02 * gate_opening[1] + 0.0000001  # Hull 2 tverrsnittareal (m^2)
    A_h3 = 0.02 * gate_opening[2] + 0.0000001

    if dagsfaktor % 60 == 0:
        if dagsfaktor / 60 >= 5:
            nedbør_log.append(nedbør(dag))
        ran1 = True
        dag += 1

    #Vær tekst
    if ran1 == True:
        message_display("Nedbør i dag: {}".format(nedbør_log[dag - 1]), 20, 1030, 380)
        message_display(str(nedbør_log[dag]), 20, 1098, 410)
        message_display(str(nedbør_log[dag + 1]), 20, 1098, 440)

    #Vær animasjon
    vær_regn = nedbør_log[dag - 1] + nedbør_log[dag] + nedbør_log[dag + 1]
    if vær_regn < 3:
        gameDisplay.blit(solImg,(970,460))
    elif vær_regn >= 3 and vær_regn < 12:
        gameDisplay.blit(sol_skyImg,(970,460))
    elif vær_regn >= 12 and vær_regn < 30:
        gameDisplay.blit(sol_sky_regnImg, (970,460))

    q_inn1 = nedbør_log[dag - 1]

    spin(gate_opening[0],1)
    spin(gate_opening[1],2)
    spin(gate_opening[2],3)

    #Propell 1 animasjon
    prop_Img = pygame.transform.rotate(propImg, spinn[0])
    D_1 = spin_2(spinn[0])
    gameDisplay.blit(prop_Img, (D_1+287, D_1+175))
    #Propell 2 animasjon
    prop_Img = pygame.transform.rotate(propImg, spinn[1])
    D_2 = spin_2(spinn[1])
    gameDisplay.blit(prop_Img, (D_2 + 667, D_2 + 175))
    #Propell 3 animasjon
    prop_Img = pygame.transform.rotate(propImg, spinn[2])
    D_3 = spin_2(spinn[2])
    gameDisplay.blit(prop_Img, (D_3 + 1047, D_3 + 175))

    vannstand(160, h_1 / 1, 80, 195, dark_blue)
    vannstand(160, h_2 / 1, 460, 195, dark_blue)
    vannstand(160, h_3 / 1, 840, 195, dark_blue)

    gameDisplay.blit(damImg,(70,50))
    gameDisplay.blit(damImg,(450,50))
    gameDisplay.blit(damImg,(830,50))

    #Tegner minimumsvannstand-streker
    pygame.draw.rect(gameDisplay,red,(70, 195 - min_vann_1,178,2))
    pygame.draw.rect(gameDisplay, red, (450, 195 - min_vann_2, 178, 2))
    pygame.draw.rect(gameDisplay, red, (830, 195 - min_vann_3, 178, 2))
    #Tegner maksimumsvannstand-streker
    pygame.draw.rect(gameDisplay, green, (70, 195 - max_vann_1, 178, 2))
    pygame.draw.rect(gameDisplay, green, (450, 195 - max_vann_2, 178, 2))
    pygame.draw.rect(gameDisplay, green, (830, 195 - max_vann_3, 178, 2))

    if tid > 0 and h_1 > 0 and h_2 > 0 and h_3 > 0: # ingen beregning ved t = 0, der bruker vi initialverdier
        h_1 = euler(h_1, stigning(A_h1, A_t1, h_1, q_inn1), dt)
        v_1 = hastighet(h_1) # Hastigheten til væsken som strømmer ut av hullet
        q_inn2 = A_h1 * v_1 # Mengden væske som strømmer ut av hullet i tank 1
        h_2 = euler(h_2, stigning(A_h2, A_t2, h_2, q_inn2), dt)
        v_2 = hastighet(h_2)  # Hastigheten til væsken som strømmer ut av hullet
        q_inn3 = A_h2 * v_2  # Mengden væske som strømmer ut av hullet i tank 1
        h_3 = euler(h_3, stigning(A_h3, A_t3, h_3, q_inn3), dt)
        v_3 = hastighet(h_3)
        q_ut3 = A_h3 * v_3

    if h_1 <= min_vann_1 or h_2 <= min_vann_2 or h_3 <= min_vann_3:
        game_over()

    #Sjekker om det er for mye vann i tanken
    if max_vann_1 < h_1:
        if buffer_1 > 0:
            message_display_2(str(buffer_1),35,330,60,red)
            if dagsfaktor % 15 == 0:
                buffer_1 -= 1
        else:
            game_over()
    elif max_vann_2 < h_2:
        message_display_2(str(buffer_2), 35, 730, 60, red)
        if buffer_2 > 0:
            if dagsfaktor % 15 == 0:
                buffer_2 -= 1
        else:
            game_over()
    elif max_vann_3 < h_3:
        message_display_2(str(buffer_3), 35, 1100, 60, red)
        if buffer_3 > 0:
            if dagsfaktor % 15 == 0:
                buffer_3 -= 1
        else:
            game_over_high()
    else:
        buffer_1, buffer_2, buffer_3 = 5,5,5


    t_hist.append(t)
    h1_hist.append(h_1)
    h2_hist.append(h_2)
    h3_hist.append(h_3)
    tid += dt

    #Legger til kapitalen du kan kjøpe med
    kapital += strøm(q_inn2,virkningsgrad_1,strømpris(dag))
    kapital += strøm(q_inn3, virkningsgrad_2, strømpris(dag))
    kapital += strøm(q_ut3, virkningsgrad_3, strømpris(dag))
    #Legger til kapitalen til en skjult info som brukes i scoren
    hidden_kapital += strøm(q_inn2, virkningsgrad_1, strømpris(dag))
    hidden_kapital += strøm(q_inn3, virkningsgrad_2, strømpris(dag))
    hidden_kapital += strøm(q_ut3, virkningsgrad_3, strømpris(dag))


    #Tegner kapasitet på beholder vinduene
    message_display_2('Kapasitet {} %'.format(round(gate_opening[0],0)), 20, 70, 200)
    message_display_2('Kapasitet {} %'.format(round(gate_opening[1],0)), 20, 450, 200)
    message_display_2('Kapasitet {} %'.format(round(gate_opening[2],0)), 20, 830, 200)
    #Tegenr kapasitet på vannbeholder
    message_display_2('Total kapasitet {} L'.format(A_t1 * max_vann_1), 20, 70, 230)
    message_display_2('Total kapasitet {} L'.format(A_t2 * max_vann_2), 20, 450, 230)
    message_display_2('Total kapasitet {} L'.format(A_t3 * max_vann_3), 20, 830, 230)

    message_display(moneynator(kapital)+ 'kr',40,600,360)

    dagen, maander, aar = dato(dag)
    message_display('{}.'.format(str(dagen)), 60, 180, 490)
    message_display(str(maander),35,180,540)
    message_display(str(aar),20,180,575)

    #Tegner puse og mute knapp
    button_Img(1165,5,30,30,ac_pauImg,in_pauImg,pause)
    mute_button(1125,5,30,30,muteImg,nonmuteImg)

    #Oppgraderingskrav
    oppgrad_res_1 = 10000 * (oppg_key_1 ** 5)
    oppgrad_res_2 = 10000 * (oppg_key_2 ** 5)
    oppgrad_res_3 = 10000 * (oppg_key_3 ** 5)
    #Tegbner knapper for oppgradeinger
    if oppgrad_res_1 <= kapital :
        circle_button('1', 646, 663, 22,red,dark_red,oppgrader_1)
    else:
        circle_button('1', 646, 663, 22, dark_red,dark_red)

    if oppgrad_res_2 <= kapital:
        circle_button('2', 720, 663, 22,red,dark_red,oppgrader_2)
    else:
        circle_button('2', 720, 663, 22, dark_red,dark_red)

    if oppgrad_res_3 <= kapital:
        circle_button('3', 793, 663, 22,red,dark_red,oppgrader_3)
    else:
        circle_button('3', 793, 663, 22, dark_red,dark_red)
    #Teger effektiviteten på pumpene
    message_display_2('Pumpe 1:     {} %'.format(round(virkningsgrad_1 * 100, 0)), 15, 690, 500, white)
    message_display_2('Pumpe 2:     {} %'.format(round(virkningsgrad_2 * 100, 0)), 15, 690, 530, white)
    message_display_2('Pumpe 3:     {} %'.format(round(virkningsgrad_3 * 100, 0)), 15, 690, 560, white)
    finn = random.randrange(2*10**50)
    if finn == 20:
        Event()
        print('Nice')

next = game_intro

while True:
    knapp = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    click_prev = clicked[0]
    clicked = pygame.mouse.get_pressed()
    click = clicked[0]-click_prev

    next()

    pygame.display.update()
    clock.tick(fps)
    gameDisplay.fill(white)