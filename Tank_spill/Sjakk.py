"""
Sjakk laget av Vegard Ervik
Kun til visning til studass
"""


black_pieces = ['k','q','r','n','b','y'] #Sorte brikker
white_pieces = ['K','Q','R','N','B','P'] #Hvite brikker

def make_board(board_string):
    x = list(board_string)
    output = []
    for i in range(5):
        rad = []
        for j in range(5):
            if x[0] == ".":
                rad.append(("-"))
            else:
                rad.append(x[0])
            del x[0]
        output.append(rad)
    return output

def board_print(board):
    print("______________________")
    for i in range(5):
        rad = board[i]
        for j in range(5):
            if j == 0:
                print(abs(i-5), end ='\t' )
            print(str(rad[j]), end='\t')
        print ()
    print("\t1\t2\t3\t4\t5")
    print("______________________")
    print()

def change_piece(board, x, y, new_piece):
    y_verdi = board[5-y]
    y_verdi [x-1] = new_piece
    board[5-y] = y_verdi
    return board

def get_piece(board, x, y):
    if x < 1 or y < 1:
        return None
    if y >= 6 or x >= 6:
        return None
    try:
        y_verdi = board[5-y]
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
        elif y == 5: #Hvis bonden står på enden av banen
            print("No legal moves")
            return
        else: #Gjelder for y-verdiene 3 og 4
            if get_piece(board, x, y+1) == ("-"):
                legal_moves.append((x,y+1))
        if x == 1: #Sjekker for skråbevegelser når brikken står inntil venstre side
            if (get_piece(board, x+1, y+1) in black_pieces):
                legal_moves.append((x+1, y+1))
        elif x == 5: #Sjekker for skråbevegelser når brikken står inntil høyre side
            if (get_piece(board, x-1, y+1) in black_pieces):
                legal_moves.append((x-1,y+1))
        else: #Sjekker hvis den ikke står innat en kant
            if (get_piece(board, x-1, y+1) in black_pieces):
                legal_moves.append((x-1,y+1))
            if (get_piece(board, x + 1, y + 1) in black_pieces):
                legal_moves.append((x + 1, y + 1))
    if piece == "y":  #Denne if'en gjelder for sorte bønder
        if y == 4: #Hvis bonden står i startposisjonen sin, sjekker for om den kan gå frem
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
            if (get_piece(board, x+1, y-1) in white_pieces):
                legal_moves.append((x+1, y-1))
        elif x == 5: #Sjekker for skråbevegelser når brikken står inntil høyre side
            if (get_piece(board, x-1, y-1) in white_pieces):
                legal_moves.append((x-1,y-1))
        else:
            if (get_piece(board, x-1, y-1) in white_pieces):
                legal_moves.append((x-1,y-1))
            if (get_piece(board, x + 1, y - 1) in white_pieces):
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
            if get_piece(board, x+a, y+a) == ("-"):
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
            if get_piece(board, x-a, y+a) == ("-"):
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
            if get_piece(board, x+a, y-a) == ("-"):
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
            if get_piece(board, x-a, y-a) == ("-"):
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
                elif piece == ("-"):
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
                elif piece == ("-"):
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
                elif piece == ("-"):
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
                elif piece == ("-"):
                    legal_moves.append((x+a,y))
                else:
                    right = False
            except:
                right = False
    return legal_moves

def get_legal_moves_king(board, x, y, opp_p_color):
    legal_moves = []
    try:
        if get_piece(board, x+1, y+1) == ("-") or get_piece(board, x+1, y+1) in opp_p_color:
            legal_moves.append((x+1, y+1))
        if get_piece(board, x + 1, y) == ("-") or get_piece(board, x+1, y) in opp_p_color:
            legal_moves.append((x + 1, y))
        if get_piece(board, x + 1, y - 1) == ("-") or get_piece(board, x+1, y-1) in opp_p_color:
            legal_moves.append((x + 1, y - 1))
        if get_piece(board, x, y - 1) == ("-") or get_piece(board, x, y-1) in opp_p_color:
            legal_moves.append((x , y - 1))
        if get_piece(board, x - 1, y - 1) == ("-") or get_piece(board, x - 1, y - 1) in opp_p_color:
            legal_moves.append((x - 1, y - 1))
        if get_piece(board, x - 1, y) == ("-") or get_piece(board, x - 1 , y) in opp_p_color:
            legal_moves.append((x - 1, y))
        if get_piece(board, x -1 , y + 1) == ("-") or get_piece(board, x - 1, y + 1) in opp_p_color:
            legal_moves.append((x - 1, y + 1))
        if get_piece(board, x, y + 1) == ("-") or get_piece(board, x, y + 1) in opp_p_color:
            legal_moves.append((x, y + 1))
    except:
        ("-")
    return legal_moves

def get_legal_moves_knight(board, x, y, opp_p_color):
    legal_moves = []
    try:
        if get_piece(board, x+1, y+2) == ("-") or get_piece(board, x+1, y+2) in opp_p_color:
            legal_moves.append((x+1, y+2))
        if get_piece(board, x + 1, y-2) == ("-") or get_piece(board, x+1, y-2) in opp_p_color:
            legal_moves.append((x + 1, y-2))
        if get_piece(board, x + 2, y + 1) == ("-") or get_piece(board, x+2, y+1) in opp_p_color:
            legal_moves.append((x + 2, y + 1))
        if get_piece(board, x - 2, y + 1) == ("-") or get_piece(board, x - 2, y+1) in opp_p_color:
            legal_moves.append((x - 2, y + 1))
        if get_piece(board, x-1, y+2) == ("-") or get_piece(board, x-1, y+2) in opp_p_color:
            legal_moves.append((x - 1, y + 2))
        if get_piece(board, x - 1, y - 2) == ("-") or get_piece(board, x - 1 , y - 2) in opp_p_color:
            legal_moves.append((x - 1, y - 2))
        if get_piece(board, x + 2 , y - 1) == ("-") or get_piece(board, x + 2, y - 1) in opp_p_color:
            legal_moves.append((x + 2, y - 1))
        if get_piece(board, x - 2, y - 1) == ("-") or get_piece(board, x - 2, y - 1) in opp_p_color:
            legal_moves.append((x - 2, y - 1))
    except:
        None
    return legal_moves

board_string = 'rnkbqyyyyy.....PPPPPRNKBQ'
board = make_board(board_string)

def main():
    print("""Dette spillet er laget av VegardE
Ha det gøy
Copyright 2019 elns
    """)
    board = make_board(board_string)
    while True:                             #Gameløkke
        board_print(board)
        print("Hvit sin tur")
        while True:   #Denne loopen er nødvendig i tilfelle brikken ikke kan bevege seg
            while True:                         #Brikkevalg for hvit
                xkord = int(input("Hvilket x-koordinat står brikken du vil flytte på?: "))
                ykord = int(input("Hvilket y-koordinat står brikken du vil flytte på?: "))
                try:
                    if get_piece(board, xkord, ykord) in white_pieces:
                        break
                    else:
                        print("Ugyldig input")
                except:
                    print("Uglydig input")
            piece = get_piece(board, xkord, ykord)
            if piece == "R":
                legal_moves = get_legal_moves_rook(board, xkord, ykord, black_pieces)
            elif piece == "N":
                legal_moves = get_legal_moves_knight(board, xkord, ykord, black_pieces)
            elif piece == "B":
                legal_moves = get_legal_moves_pawn(board, xkord, ykord, black_pieces)
            elif piece == "Q":
                legal_moves = get_legal_moves_rook(board, xkord, ykord, black_pieces) + get_legal_moves_bishop(board, xkord, ykord, black_pieces)
            elif piece == "K":
                legal_moves = get_legal_moves_king(board, xkord, ykord, black_pieces)
            else:
                legal_moves = get_legal_moves_pawn(board, xkord, ykord)
            if legal_moves:
                break
            else:
                print("Ingen gyldige trekk")
        while True:
            print("Dine gyldige trekk er:", legal_moves)
            xflytt = int(input("Til hvilket x-koordinat vil du flytte brikka?"))
            yflytt = int(input("Til hvilket y-koordinat vil du flytte brikka?"))
            flytt = (xflytt, yflytt)
            if flytt in legal_moves:
                break
            else:
                print("Ugyldig trekk")
        board = change_piece(board, xkord, ykord, "-")
        board = change_piece(board, xflytt, yflytt, piece)

        board_print(board)
        print("Sort sin tur")
        while True:  # Denne loopen er nødvendig i tilfelle brikken ikke kan bevege seg
            while True:  # Brikkevalg for sort
                xkord = int(input("Hvilket x-koordinat står brikken du vil flytte på?: "))
                ykord = int(input("Hvilket y-koordinat står brikken du vil flytte på?: "))
                try:
                    if get_piece(board, xkord, ykord) in black_pieces:
                        break
                    else:
                        print("Ugyldig input")
                except:
                    print("Uglydig input")
            piece = get_piece(board, xkord, ykord)
            if piece == "r":
                legal_moves = get_legal_moves_rook(board, xkord, ykord, white_pieces)
            elif piece == "n":
                legal_moves = get_legal_moves_knight(board, xkord, ykord, white_pieces)
            elif piece == "b":
                legal_moves = get_legal_moves_pawn(board, xkord, ykord, white_pieces)
            elif piece == "q":
                legal_moves = get_legal_moves_rook(board, xkord, ykord, white_pieces) + get_legal_moves_bishop(board,
                                                                                                               xkord,
                                                                                                               ykord,
                                                                                                               white_pieces)
            elif piece == "k":
                legal_moves = get_legal_moves_king(board, xkord, ykord, white_pieces)
            else:
                legal_moves = get_legal_moves_pawn(board, xkord, ykord)
            if legal_moves:
                break
            else:
                print("Ingen gyldige trekk")
        while True:
            print("Dine gyldige trekk er:", legal_moves)
            xflytt = int(input("Til hvilket x-koordinat vil du flytte brikka?"))
            yflytt = int(input("Til hvilket y-koordinat vil du flytte brikka?"))
            flytt = (xflytt, yflytt)
            if flytt in legal_moves:
                break
            else:
                print("Ugyldig trekk")
        board = change_piece(board, xkord, ykord, "-")
        board = change_piece(board, xflytt, yflytt, piece)

main()