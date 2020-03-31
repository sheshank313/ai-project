def game_board():
    return([['-','-','-'],
        ['-','-','-'],
        ['-','-','-']])
# Game Show
def show_board(board):
    for i in board:
        for j in i:
            print(j,end='\t')
        print()

    print()

def empty_places(board):
    
    for i in range(len(board)): 
        for j in range(len(board)): 
            
            if board[i][j] == '-': 
                return True
    return False

def findBestMove(board,player_turn,win_game):
        bestscore = -100
        bestMove = [None,None]

        for i in range(3):
                #print(i,end=' - ')
                for j in range(3):
                        #print(j,end='-')
                        if(board[i][j]=='-'):
                                #print(j,end='*')
                                board[i][j] = ai
                                score,win_game = minmax(board,0,False,win_game)
                                board[i][j] = '-'
                                #print(score)
                                if(score > bestscore):
                                        #print(j,end='+')
                                        #print(score)
                                        bestscore = score
                                        bestMove = [i,j]
                                

        board[bestMove[0]][bestMove[1]] = ai
        player_turn = True
        return board,player_turn


def minmax(board,depth,isMAx,win_game):
        #print(winner_check(board,win_game))
        win_game = winner_check(board,win_game)
        if(win_game == human):
            return -1,human

        if(win_game == ai):
            return 1,ai

        if(empty_places(board)==False):
            return 0,'Tied'

        if(isMAx):
                best = -10
                for i in range(3):
                        for j in range(3):
                                if(board[i][j] == '-'):
                                        board[i][j] = ai
                                        score,win_game = minmax(board,depth+1,False,win_game)
                                        best = max(best,score)
                                        board[i][j] = '-'
                                        #print(best)
                                        #print(win_game)
                                        #show_board(board)
                                        #print(i,j)
                return best,win_game

        else:
                best = 10
                for i in range(3):
                        for j in range(3):
                                if(board[i][j] == '-'):
                                        board[i][j] = human
                                        score,win_game = minmax(board,depth+1,True,win_game)
                                        best = min(best,score)
                                        board[i][j] = '-'
                                        #print(best)
                return best,win_game
        

def winner_check(board,win_game):
    win_game = None
    for i in range(3):
        if(board[i][1]!='-' and board[i][0]==board[i][1] and board[i][1]==board[i][2]):
            win_game = board[i][1]

        elif(board[1][i]!='-' and board[0][i]==board[1][i] and board[1][i]==board[2][i]):
            win_game = board[1][i]

        elif(board[1][1]!='-'):
            if(board[0][0]==board[1][1] and board[1][1]==board[2][2]):
                win_game = board[1][1]

            elif(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
                win_game = board[1][1]

    if(win_game==None):
        win_game = '-'

    return win_game

def players_turn(board):
    try:
        move = int(input("Enter the number of poisition to play:"))
        move = move - 1
        col = move%3
        row = move//3
        if(board[row][col]=='-' and move>=0):
            board[row][col] = human
        elif(move<0):
            print("Please enter a p+ve number.\n")
            players_turn(board)
        else:
            print("Please select a blank Space ")
            players_turn(board)
    except (IndexError,ValueError):
        print("Enter a number between 0-9")
        players_turn(board)
    player_turn = False

    return board,player_turn

def move2():
    human = ''
    while human!='O' and human!='X':
        try:
            human = input("You want to go with X or O :")
            human = human.upper()
            if(human =='X'):
                ai = 'O'
            else:
                ai = 'X'  
        except TypeError:
            move2()

    return human,ai

def turn2():
    turn = ''
    while turn != 'Y' and turn != 'N':
        try:
            turn = input("Press Y to go first else press N.")
            turn = turn.upper()
            if(turn=='Y'):
                player_turn = True
            else:
                player_turn = False
        except (KeyError,ValueError):
            turn2()
    return player_turn
def play_game():
    board = game_board()
    win_game = '-'
    count = 0
    temp = 1
    global human,ai
    human,ai = move2()
    player_turn = turn2()
    print("Below poistion number are shown as you want to move.") 
    for i in board:
        for j in i:
            print(temp,end='\t')
            temp += 1
        print()

    print()

    while(win_game == '-' and count<9):
        if(player_turn == True):
            board,player_turn = players_turn(board)
            win_game = winner_check(board,win_game)
            print("Player's Move.")
            show_board(board)
            temp = 0

        else:
            print("Computer's Move.")
            board,player_turn = findBestMove(board,player_turn,win_game)
            win_game = winner_check(board,win_game)
            show_board(board)
            temp = 1

        count += 1

    if(count==9):
            print("Match Tied.")

    elif(count<9):
            if(temp==1):
                print("System wins.")
            else:
                print("Human wins.")
play_game()





