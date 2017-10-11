#konge: k, dronning: q, tårn: r, løper: b, hest: n, bonde: p
board_size = 5

def make_board(board_string):
    global board_size
    board = []
    for i in range(0, board_size):
        line = []
        for j in range(0, board_size):
            current = board_string[j + i * board_size]
            if(current != "."):
                line.append(current)
            else:
                line.append(None)
        board.append(line)

    return board


def get_piece(board, x, y):
    x -= 1
    y -= 1
    x, y = y, x
    return list(reversed(board))[x][y]


def get_legal_moves(board, x, y):
    piece = get_piece(board, x, y)
    print(piece)
    if(piece == "p" or piece == "P"):
        moves = []
        if(piece == "P"):
            if(not(get_piece(board, x, y + 1))):
                #Kan gå rett frem (1)
                moves.append((x, y + 1))

            left = get_piece(board, x + 1, y + 1)
            right = get_piece(board, x - 1, y + 1)
            front = get_piece(board, x, 4)

            if(left):
                if(left.islower()):
                    #Kan angripe venstre
                    moves.append((x + 1, y + 1))

            if(right):
                if(right.islower()):
                    #Kan angripe høyre
                    moves.append((x - 1, y + 1))

            if(y == 2 and not(front)):
                #startpos
                moves.append((x, y + 2))
        else:
        #piece == "p"
            if(not(get_piece(board, x, y - 1))):
                #Kan gå rett frem (1)
                moves.append((x, y - 1))

            left = get_piece(board, x - 1, y - 1)
            right = get_piece(board, x + 1, y - 1)
            front = get_piece(board, x, 4)

            if(left):
                if(left.isupper()):
                    #Kan angripe venstre
                    moves.append((x - 1, y - 1))

            if(right):
                if(right.isupper()):
                    #Kan angripe høyre
                    moves.append((x + 1, y - 1))


            if(y == 4 and not(front)):
                #startpos
                moves.append((x, y - 2))

        return moves
    else:
        return None


print(board = make_board("rkn.r.p.....P..PP.PPB.K.."))
print(get_piece(board, 4, 2))
print(get_legal_moves(board, 4, 2))
