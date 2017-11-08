def print_board(board):
    print(" "*3, "1", " ", "2", " ", "3")
    print(" ","-"*13)
    for i, line in enumerate(board):
        print(i+1, "|",line[0],"|",line[1],"|",line[2],"|")
        print(" ","-"*13)


def check_horizontal(board):
    won = False
    won_char = ""
    for line in board:
        won = False
        for i in range(len(line) - 1):
            if(line[i] == line[i + 1]):
                won = True
                won_char = line[i]
            else:
                won = False
    return [won, won_char]


def check_vertical(board):
    won = False
    won_char = ""
    for i in range(len(board) - 1):
        won = False
        for j in range(len(board[i])):
            if(board[i][j] == board[i + 1][j]):
                won = True
                won_char = board[i][j]
            else:
                won = False
    return [won, won_char]


def check_diagonal(board):
    diagonal_right = board[0][2] == board[1][1] and board[1][1] == board[2][0]
    diagonal_left = board[0][0] == board[1][1] and board[1][1] == board[0][2]
    return [diagonal_left or diagonal_right, board[1][1]]


def check_win(board, players):
    full = [check_horizontal(board), check_vertical(board), check_diagonal(board)]
    for check in full:
        if(check[0]):
            print_win(check, players)
            return True
    else:
        return False


def print_win(check, players):
    if(check[1] == "x"):
        #Player 1 won
        print(players[1], "vant!")
    else:
        print(players[0], "vant!")
    return True


def get_players():
    players = []
    players.append(input("Skriv inn navnet til spiller 1: "))
    players.append(input("Skriv inn navnet til spiller 2: "))
    return players


def check_move(board, x, y):
    #Board is an array of the board
    if(board[x-1][y-1] != " " or x > 3 or x < 1 or y > 3 or y < 1):
        print("Ulovlig trekk!")
        return False
    return True


def new_board():
    board = []
    for line in range(3):
        new = []
        for i in range(3):
            new.append(" ")
        board.append(new)
    return board


def new_game():
    board = new_board()
    players = get_players()
    return board, players


def move(board, player, x, y):
    if(player == 1):
        if(check_move(board, x, y)):
            board[x-1][y-1] = "x"
    else:
        if(check_move(board, x, y)):
            board[x-1][y-1] = "o"


def main():
    board, players = new_game()
    i = 0
    won = False
    while not(won):
        try:
            print_board(board)
            print(players[i%2], "sin tur")
            x = int(input("Skriv inn x koordinat: "))
            y = int(input("Skriv inn y koordinat: "))
            if(i % 2 == 0):
                #Spiller 1 sin tur
                move(board, 1, x, y)
            else:
                #Spiller 2 sin tur
                move(board, 2, x, y)
            i += 1
            won = check_win(board, players) and i > 4
        except:
            print("Du skrev ikke inn et heltall!")
main()
