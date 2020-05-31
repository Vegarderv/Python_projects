import pygame
import funk
import PyGame_funksjoner as pyf

#Her legger jeg variabler som er nødvendige for at spillet skal fungere
farger = {'brun' : (160,82,45), 'hvit' : (225, 225, 195)}
r_side = 80
bredde = r_side
høyde = r_side
bleed = 60
bokstaver = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
surface = pygame.image.load('surface.png')
pygame.mixer_music.load('musikk.mp3')

#Dette er pygamevariabler
run = True
fps = 60
klokke = int(1000/fps)
move = False
timer = 0


#Disse starter pygame
pygame.init()
window = pygame.display.set_mode((r_side*8 + bleed, r_side*8 + bleed))
pygame.display.set_caption("PySjakk")
pygame.display.set_icon(surface)

window.fill((210, 240, 210))
pyf.drawBoard(window, r_side, bleed)  #Funksjon fra PyGame_funksjoner som tegner brettet, må muligens oppdateres for å tegne farger
pyf.drawPieces(funk.board, window, r_side, bleed)
pygame.display.update()

moved = True
oppdate = False
flytt = False
check = False
rokadeliste = [99999]



pygame.mixer_music.play(0,0)
#Game-løkke
while run:        #GameLøkke
    pygame.time.delay(klokke)
    for event in pygame.event.get():  #Eventløkke, sjekker om brukeren trykker noe sted
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Denne ifen sjekker om en av rutene blir trykket på
            if event.button == 1:  # Venstre museknapp.
                # Sjekker om musen er innenfor runta
                pos = list(pygame.mouse.get_pos())

                if not moved:
                    x = int((pos[0]-bleed)/r_side) + 1
                    y = abs(int(pos[1]/r_side) - 8)
                    move = (x, y)
                    if legal_moves:
                        if move in legal_moves:
                            rokadeliste = funk.rokadeliste(funk.board, x_pos, y_pos, rokadeliste)
                            pyf.movePiece(funk.board, x_pos, y_pos, brikke, x, y)
                            moved = True
                            legal_moves = []
                            oppdate = True
                            check = funk.chech_if_check(funk.board)
                            if check:
                                funk.check_if_cm(funk.board, timer)
                            timer += 1
                        else:
                            moved = True
                            oppdate = True
                            legal_moves = []
                if moved:
                    try:
                        brikke, x_pos, y_pos = pyf.getPiece(funk.board, pos[0], pos[1], r_side, bleed)
                    except:
                        None
                    if timer % 2 == 0:
                        if brikke in funk.white_pieces:
                            flytt = True
                    else:
                        if brikke in funk.black_pieces:
                            flytt = True
                    if flytt:
                        legal_moves = funk.get_legal_moves(funk.board, x_pos, y_pos, brikke, check, rokadeliste)
                        flytt = False
                        if legal_moves:
                            moved = False
                            oppdate = True
    if oppdate:
        window.fill((210, 240, 210))
        pyf.drawBoard(window, r_side, bleed, legal_moves)
        pyf.drawPieces(funk.board, window, r_side, bleed)
        pygame.display.update()      #

