import pygame
import funk
import time
farger = {'brun': (160, 82, 45), 'hvit': (225, 225, 195)}
bokstaver = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
pygame.init()


def PyTekst(tekst, farge, bakgrunnsfarge, size, x, y, rectlen):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(tekst, True, farge, bakgrunnsfarge)
    textRect = text.get_rect()
    textRect.center = (x // 2 + rectlen // 2, y // 2 + rectlen // 2)
    return text, textRect

def drawBoard(window, r_side, bleed, legal_moves = None):
    farger = {'brun': (160, 82, 45), 'hvit': (225, 225, 195)}
    a = 0
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            x_rect = x * r_side + bleed
            y_rect = y * r_side
            if legal_moves:
                move = (x + 1, abs(y - 8))
                if move in legal_moves:
                    farger['hvit'] = (255, 0, 100)
                    farger['brun'] = (255, 100, 0)
            if i % 2 == 0:  # Denne ifen printer rutene på brettet
                if j % 2 != 0:
                    pygame.draw.rect(window, farger['brun'], (x_rect, y_rect, r_side, r_side))
                else:
                    pygame.draw.rect(window, farger['hvit'], (x_rect, y_rect, r_side, r_side))
            else:
                if j % 2 == 0:
                    pygame.draw.rect(window, farger['brun'], (x_rect, y_rect, r_side, r_side))
                else:
                    pygame.draw.rect(window, farger['hvit'], (x_rect, y_rect, r_side, r_side))
            x += 1
            farger = {'brun': (160, 82, 45), 'hvit': (225, 225, 195)}
        tall, tall_pos = PyTekst(str(abs(i - 8)), (0, 0, 0), (210, 240, 210), 40, bleed, y * r_side * 2 + r_side, 0)
        window.blit(tall, tall_pos)
        y += 1
        a += 1
    for i in range(8):
        boks, boks_pos = PyTekst(bokstaver[i], (0, 0, 0), (210, 240, 210), 40, (bleed + i * r_side) * 2 + r_side,
                                     680 * 2 - 20, 0)
        window.blit(boks, boks_pos)

def getPiece(board, xpos, ypos, r_side, bleed):
    for i in range(8):
        for j in range(8):
            if (bleed + (r_side * j)) <= xpos and ((bleed + (r_side * j)) + r_side) >= xpos:
                if ypos >= ( r_side * i) and ypos <= ((r_side * i) + r_side):
                    y = board[i]
                    return y[j], j + 1, abs(i-8)

def drawPieces(board, window, r_side, bleed):
    a = 0
    y = 0
    for i in range(8):
        rad_x = board[i]
        x = 0
        for j in range(8):
            x_rect = x * r_side + bleed
            y_rect = y * r_side
            brikke = rad_x[j]
            if brikke != '-' and brikke != 'o':  # Denne ifen printer brikkene
                if brikke in funk.black_pieces:
                    disp, rect = PyTekst(brikke, (255, 255, 255), (0, 0, 0), 40, x_rect * 2, y_rect * 2, r_side)
                else:
                    disp, rect = PyTekst(brikke, (0, 0, 0), (255, 255, 255), 40, x_rect * 2, y_rect * 2, r_side)
                window.blit(disp, rect)
            x += 1
        y += 1
        a += 1

def movePiece(board, prev_xpos, prev_ypos, piece, xpos, ypos):
    if piece == 'P' and ypos == 8:   #Transformasjon for hvite bønder
        piece = 'Q'
    elif piece == 'y' and ypos == 1: #Transformasjon for sorte bønder
        piece = 'q'
    brikken = funk.get_piece(board, xpos, ypos)  #Denne letter etter 'o'
    if brikken == 'o' and ypos == 3:     #Denne sletter brikken foran oen dersom passant skal gjennomføres
        funk.change_piece(board, xpos, 4, '-')
    if brikken == 'o' and ypos == 6:
        funk.change_piece(board, xpos, 5, '-')
    funk.change_piece(board, prev_xpos, prev_ypos, "-")  #Denne bytter brikkene
    funk.change_piece(board, xpos, ypos, piece)
    for i in range(8): #Denne sletter oene bak bøndene som beger seg to opp, slik at passant bare fungerer en runde
        y = abs(i-8)
        rad = board[i]
        for j in range(8):
            x = j + 1
            if funk.get_piece(board, x, y) == "o":
                rad[j] = '-'
    if piece == 'P' and ypos == 4 and prev_ypos == 2:  #Denne legger til en 'o' bak en bonde som beveger seg 2 frem i et passanttilfelle
        funk.change_piece(board, xpos, 3, "o")
    elif piece == "y" and ypos == 5 and prev_ypos == 7:
        funk.change_piece(board, xpos, 6, "o")
    if piece == "K" and abs(xpos - prev_xpos) >= 2:  #Denne ifen ordner med rokade
        if xpos == 7:
            funk.change_piece(board, 8, 1, "-")
            funk.change_piece(board, 6, 1, 'R')
        else:
            funk.change_piece(board, 1, 1, "-")
            funk.change_piece(board, 3, 1, 'R')
    if piece == "k" and abs(xpos - prev_xpos) >= 2:
        if xpos == 7:
            funk.change_piece(board, 8, 8, "-")
            funk.change_piece(board, 6, 8, 'r')
        else:
            funk.change_piece(board, 1, 8, "-")
            funk.change_piece(board, 3, 8, 'r')

