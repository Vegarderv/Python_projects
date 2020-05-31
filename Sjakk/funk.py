"""
Sjakk laget av Vegard Ervik
Kun til visning til studass
"""

import copy

black_pieces = ['k','q','r','n','b','y'] #Sorte brikker
white_pieces = ['K','Q','R','N','B','P'] #Hvite brikker

def make_board(board_string):
    x = list(board_string)
    output = []
    for i in range(8):
        rad = []
        for j in range(8):
            if x[0] == ".":
                rad.append(("-"))
            else:
                rad.append(x[0])
            del x[0]
        output.append(rad)
    return output

def board_print(board):
    print("______________________")
    for i in range(8):
        rad = board[i]
        for j in range(8):
            if j == 0:
                print(abs(i-8), end ='\t' )
            print(str(rad[j]), end='\t')
        print ()
    print("\t1\t2\t3\t4\t5\t6\t7\t8")
    print("______________________")
    print()

def change_piece(board, x, y, new_piece):
    y_verdi = board[8-y]
    y_verdi [x-1] = new_piece
    board[8-y] = y_verdi
    return board

def get_piece(board, x, y):
    if x < 1 or y < 1:
        return None
    if y >= 9 or x >= 9:
        return None
    try:
        y_verdi = board[8-y]
    except:
        return None
    return (y_verdi[x-1])

def get_legal_moves_pawn(board, x, y): #Funksjon som sjekker lovlige trekk for bønder
    piece = get_piece(board, x, y) #Finner navnet på brikken
    legal_moves = [] #Liste som skal inneholde lovlige trekk, blir output
    if piece == "P":  #Denne if'en gjelder for hvite bønder
        if y == 2: #Hvis bonden står i startposisjonen sin, sjekker for om den kan gå frem
            if get_piece(board, x, y+1) == ("-"):
                legal_moves.append((x,y+1))
                if get_piece(board, x, y+2) == ("-"):
                    legal_moves.append((x,y+2))
        elif y == 8: #Hvis bonden står på enden av banen
            print("No legal moves")
            return
        else: #Gjelder for y-verdiene 3 og 4
            if get_piece(board, x, y+1) == ("-"):
                legal_moves.append((x,y+1))
        if x == 1: #Sjekker for skråbevegelser når brikken står inntil venstre side
            if (get_piece(board, x+1, y+1) in black_pieces) or (get_piece(board, x+1, y+1) == "o"):
                legal_moves.append((x+1, y+1))
        elif x == 8: #Sjekker for skråbevegelser når brikken står inntil høyre side
            if (get_piece(board, x-1, y+1) in black_pieces) or (get_piece(board, x-1, y+1) == "o"):
                legal_moves.append((x-1,y+1))
        else: #Sjekker hvis den ikke står innat en kant
            if (get_piece(board, x-1, y+1) in black_pieces) or (get_piece(board, x-1, y+1) == "o"):
                legal_moves.append((x-1,y+1))
            if (get_piece(board, x + 1, y + 1) in black_pieces) or (get_piece(board, x+1, y+1) == "o"):
                legal_moves.append((x + 1, y + 1))
    if piece == "y":  #Denne if'en gjelder for sorte bønder
        if y == 7: #Hvis bonden står i startposisjonen sin, sjekker for om den kan gå frem
            if get_piece(board, x, y-1) == ("-"):
                legal_moves.append((x,y-1))
                if get_piece(board, x, y-2) == ("-"):
                    legal_moves.append((x,y-2))
        elif y == 1: #Hvis bonden står på enden av banen
            return None
        else: #Gjelder for y-verdiene 3 og 4
            if get_piece(board, x, y-1) == ("-"):
                legal_moves.append((x,y-1))
        if x == 1: #Sjekker for skråbevegelser når brikken står inntil venstre side
            if (get_piece(board, x+1, y-1) in white_pieces) or (get_piece(board, x+1, y-1) == "o"):
                legal_moves.append((x+1, y-1))
        elif x == 8: #Sjekker for skråbevegelser når brikken står inntil høyre side
            if (get_piece(board, x-1, y-1) in white_pieces) or (get_piece(board, x-1, y-1) == "o"):
                legal_moves.append((x-1,y-1))
        else:
            if (get_piece(board, x-1, y-1) in white_pieces) or (get_piece(board, x-1, y-1) == "o"):
                legal_moves.append((x-1,y-1))
            if (get_piece(board, x + 1, y - 1) in white_pieces) or (get_piece(board, x-1, y-1) == "o"):
                legal_moves.append((x + 1, y - 1))
    if len(legal_moves) > 0:
        return (legal_moves)
    else:
        return None

def get_legal_moves_bishop(board,x,y, opp_p_color):
    legal_moves = []
    piece = get_piece(board, x, y)  # Finner navnet på brikken
    a = 0
    while True: #Sjekker om den kan bevege seg opp til høyre
        a += 1
        try:
            if get_piece(board, x+a, y+a) == ("-") or get_piece(board, x+a, y+a) == ("o"):
                legal_moves.append((x+a, y+a))
            elif get_piece(board, x+a, y+a) in opp_p_color:
                legal_moves.append((x+a, y+a))
                break
            else:
                break
        except:
            break
    a = 0
    while True: #Sjekker om den kan bevege seg opp til venstre
        a += 1
        try:
            if get_piece(board, x-a, y+a) == ("-") or get_piece(board, x-a, y+a) == ("o"):
                legal_moves.append((x-a, y+a))
            elif get_piece(board, x-a, y+a) in opp_p_color:
                legal_moves.append((x-a, y+a))
                break
            else:
                break
        except:
            break
    a = 0
    while True: #Sjekker om den kan bevege seg ned til høyre
        a += 1
        try:
            if get_piece(board, x+a, y-a) == ("-") or get_piece(board, x+a, y-a) == ("o"):
                legal_moves.append((x+a, y-a))
            elif get_piece(board, x+a, y-a) in opp_p_color:
                legal_moves.append((x+a, y-a))
                break
            else:
                break
        except:
            break
    a = 0
    while True: #Sjekker om den kan bevege seg ned til venstre
        a += 1
        try:
            if get_piece(board, x-a, y-a) == ("-") or get_piece(board, x-a, y-a) == ("o"):
                legal_moves.append((x-a, y-a))
            elif get_piece(board, x-a, y-a) in opp_p_color:
                legal_moves.append((x-a, y-a))
                break
            else:
                break
        except:
            break
    return legal_moves

def get_legal_moves_rook(board, x, y , opp_p_color):
    legal_moves = []
    up = True
    down = True
    left = True
    right = True
    a = 0
    while up or down or left or right:
        a += 1
        if up:
            try: #up
                piece = get_piece(board, x,y+a)
                if piece in opp_p_color:
                    legal_moves.append((x, y+a))
                    up = False
                elif piece == ("-") or piece == ("o"):
                    legal_moves.append((x,y+a))
                else:
                    up = False
            except:
                up = False
        if down:
            try: #down
                piece = get_piece(board, x, y-a)
                if piece in opp_p_color:
                    legal_moves.append((x, y-a))
                    down = False
                elif piece == ("-") or piece == ("o"):
                    legal_moves.append((x,y-a))
                else:
                    down = False
            except:
                down = False
        if left:
            try: #left
                piece = get_piece(board, x-a, y)
                if piece in opp_p_color:
                    legal_moves.append((x-a, y))
                    left = False
                elif piece == ("-") or piece == ("o"):
                    legal_moves.append((x-a, y))
                else:
                    left = False
            except:
                left = False
        if right:
            try: #right
                piece = get_piece(board, x+a, y)
                if piece in opp_p_color:
                    legal_moves.append((x+a, y))
                    right = False
                elif piece == ("-") or piece == ("o"):
                    legal_moves.append((x+a,y))
                else:
                    right = False
            except:
                right = False
    return legal_moves

def get_legal_moves_king(board, x, y, opp_p_color):
    legal_moves = []
    try:
        if get_piece(board, x+1, y+1) == ("-") or get_piece(board, x+1, y+1) in opp_p_color or get_piece(board, x+1, y+1) == ("o"):
            legal_moves.append((x+1, y+1))
        if get_piece(board, x + 1, y) == ("-") or get_piece(board, x+1, y) in opp_p_color or get_piece(board, x+1, y) == ("o"):
            legal_moves.append((x + 1, y))
        if get_piece(board, x + 1, y - 1) == ("-") or get_piece(board, x+1, y-1) in opp_p_color or get_piece(board, x+1, y-1) == ("o"):
            legal_moves.append((x + 1, y - 1))
        if get_piece(board, x, y - 1) == ("-") or get_piece(board, x, y-1) in opp_p_color  or get_piece(board, x, y-1) == ("o"):
            legal_moves.append((x , y - 1))
        if get_piece(board, x - 1, y - 1) == ("-") or get_piece(board, x - 1, y - 1) in opp_p_color or get_piece(board, x - 1, y - 1) == ("o"):
            legal_moves.append((x - 1, y - 1))
        if get_piece(board, x - 1, y) == ("-") or get_piece(board, x - 1 , y) in opp_p_color or get_piece(board, x-1, y) == ("o"):
            legal_moves.append((x - 1, y))
        if get_piece(board, x -1 , y + 1) == ("-") or get_piece(board, x - 1, y + 1) in opp_p_color or get_piece(board, x-1, y+1) == ("o"):
            legal_moves.append((x - 1, y + 1))
        if get_piece(board, x, y + 1) == ("-") or get_piece(board, x, y + 1) in opp_p_color or get_piece(board, x, y+1) == ("o"):
            legal_moves.append((x, y + 1))
    except:
        ("-")
    return legal_moves

def get_legal_moves_knight(board, x, y, opp_p_color):
    legal_moves = []
    try:
        if get_piece(board, x+1, y+2) == ("-") or get_piece(board, x+1, y+2) in opp_p_color  or get_piece(board, x+1, y+2) == ("o"):
            legal_moves.append((x+1, y+2))
        if get_piece(board, x + 1, y-2) == ("-") or get_piece(board, x+1, y-2) in opp_p_color  or get_piece(board, x+1, y-2) == ("o"):
            legal_moves.append((x + 1, y-2))
        if get_piece(board, x + 2, y + 1) == ("-") or get_piece(board, x+2, y+1) in opp_p_color  or get_piece(board, x+2, y+1) == ("o"):
            legal_moves.append((x + 2, y + 1))
        if get_piece(board, x - 2, y + 1) == ("-") or get_piece(board, x - 2, y+1) in opp_p_color or get_piece(board, x-2, y+1) == ("o"):
            legal_moves.append((x - 2, y + 1))
        if get_piece(board, x-1, y+2) == ("-") or get_piece(board, x-1, y+2) in opp_p_color or get_piece(board, x-1, y+2) == ("o"):
            legal_moves.append((x - 1, y + 2))
        if get_piece(board, x - 1, y - 2) == ("-") or get_piece(board, x - 1 , y - 2) in opp_p_color or get_piece(board, x-1, y-2) == ("o"):
            legal_moves.append((x - 1, y - 2))
        if get_piece(board, x + 2 , y - 1) == ("-") or get_piece(board, x + 2, y - 1) in opp_p_color or get_piece(board, x+2, y-1) == ("o"):
            legal_moves.append((x + 2, y - 1))
        if get_piece(board, x - 2, y - 1) == ("-") or get_piece(board, x - 2, y - 1) in opp_p_color or get_piece(board, x-2, y-1       ) == ("o"):
            legal_moves.append((x - 2, y - 1))
    except:
        None
    return legal_moves

def get_legal_moves(board, x, y, piece, sjakk = None, roklist = None):
    output = None
    if piece in black_pieces:
        color = white_pieces
    else:
        color = black_pieces
    if piece == "P" or piece == "y":
        output =  get_legal_moves_pawn(board, x, y)
    elif str.lower(piece) == "r":
        output = get_legal_moves_rook(board, x, y, color)
    elif str.lower(piece) == "b":
        output = get_legal_moves_bishop(board, x, y, color)
    elif str.lower(piece) == "n":
        output = get_legal_moves_knight(board, x, y, color)
    elif str.lower(piece) == "q":
        l_moves = get_legal_moves_bishop(board, x, y, color) + get_legal_moves_rook(board, x, y, color)
        output = l_moves
    elif piece == "k":
        output = get_legal_moves_king(board, x, y, color)
        if roklist:
            output += rokadesjekkersort(board, roklist)
    elif piece == "K":
        output = get_legal_moves_king(board, x, y, color)
        if roklist:
            output += rokadesjekkerhvit(board, roklist)

    if sjakk:
        legal_moves = []
        if output:
            for i in output:
                fic_board = copy.deepcopy(board)
                x_1 = i[0]
                y_1 = i[1]
                change_piece(fic_board, x_1, y_1, piece)
                change_piece(fic_board, x, y, "-")
                if not chech_if_check(fic_board):
                    legal_moves.append(i)
        output = legal_moves
    if not output:
        output = None
    return output

def chech_if_check(board):
    for i in range(8):
        y = abs(i-8)
        for j in range(8):
            x = j + 1
            if get_piece(board, x, y) == "k":
                k_pos = (x, y)
            elif get_piece(board, x, y) == "K":
                K_pos = (x, y)
    moves = []
    for i in range(8):
        y = abs(i - 8)
        for j in range(8):
            x = j + 1
            piece = get_piece(board, x, y)
            if get_legal_moves(board, x, y, piece):
                moves.append(get_legal_moves(board, x, y, piece))
    for i in moves:
        if k_pos in i:
            return True
        elif K_pos in i:
            return True

def check_if_cm(board, timer):
    if timer % 2 == 0:
        color = black_pieces
    else:
        color = white_pieces
    moves = []
    moves_pos = []
    for i in range(8):
        y = abs(i - 8)
        for j in range(8):
            x = j + 1
            piece = get_piece(board, x, y)
            if piece in color:
                if get_legal_moves(board, x, y, piece):
                    moves.append(get_legal_moves(board, x, y, piece))
                    moves_pos.append((x,y))
    checkers = False
    for j in range(len(moves)):
        prev = moves_pos[j]
        x_1 = prev[0]
        y_1 = prev[1]
        for i in moves[j]:
            curr = i
            fic_board = copy.deepcopy(board)
            x = curr[0]
            y = curr[1]
            piece = get_piece(fic_board, x_1, y_1)
            change_piece(fic_board, x, y, piece)
            change_piece(fic_board, x_1, y_1, "-")
            if not chech_if_check(fic_board):
                board_print(fic_board)
                checkers = True
    if checkers:
        return
    else:
        print("SJAKKMATT")

def rokadeliste(board ,x ,y ,liste):
    rad = board[abs(y-8)]
    brikke = rad[x-1]
    if brikke == "R" or brikke == "r" or brikke == "k" or brikke == "K":
        liste.append((brikke, x, y))
    return liste

def rokadesjekkersort(board, liste):
    output = []
    rad = board[0]
    print(liste)
    if rad[0] == 'r' and rad [1] == '-' and rad [2] == '-' and rad [3] == '-' and rad[4] == 'k':
        if ('k',5,8) not in liste and ('r', 1, 8) not in liste:
            output.append((3,8))
    if rad[7] == 'r' and rad [6] == '-' and rad [5] == '-' and rad[4] == 'k':
        if ('k',5,8) not in liste and ('r', 8, 8) not in liste:
            output.append((7,8))
    return output

def rokadesjekkerhvit(board, liste):
    output = []
    rad = board[7]
    if rad[0] == 'R' and rad [1] == '-' and rad [2] == '-' and rad [3] == '-' and rad[4] == 'K':
        if ('K',5,1) not in liste and ('R', 1, 1) not in liste:
            output.append((3,1))
    if rad[7] == 'R' and rad [6] == '-' and rad [5] == '-' and rad[4] == 'K':
        if ('K',5,1) not in liste and ('R', 8, 1) not in liste:
            output.append((7,1))
    return output

board_string = 'rnbqkbnryyyyyyyy................................PPPPPPPPRNBQKBNR'
board = make_board(board_string)
board_print(board)
