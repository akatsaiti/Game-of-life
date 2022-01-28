"""Conway\'s Game of Life."""

def board(n):
    """

    >>> game = board(3)
    >>> len(game)
    9
    >>> game
    {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}
    >>> game[2,1]
    False
    """
    
    dict={}
    for i in range(n):
        for j in range(n):
            dict[i,j]=False
    return dict



def is_alive(board, p):
    """
    >>> is_alive(board(4), (3,2))
    False
    """
    
    a=board.get(p)
    return a



def set_alive(board, p, alive):
    """

    >>> game = board(4)
    >>> is_alive(game, (3,2))
    False
    >>> set_alive(game, (3,2), True)
    >>> is_alive(game, (3,2))
    True
    >>> set_alive(game, (3,2), False)
    >>> is_alive(game, (3,2))
    False
    """
    
    board[(p)]=alive

def get_size(board):
    """

    >>> get_size(board(4))
    4
    >>> get_size(board(10))
    10
    """
   
    keys_list = list(board)
    j=0
    for i in keys_list:
        j+=1
        if i == (1,0):
            return j-1
            
            
    
def copy_board(board):
    """
    >>> game = board(10)
    >>> set_alive(game, (4,7), True)
    >>> game2 = copy_board(game)
    >>> game2 is game
    False
    >>> is_alive(game2, (4,7))
    True
    """
    
    n=get_size(board)
    copyboard={}
    for i in range(n):
        for j in range(n):
            copyboard[i,j]=board[i,j]
    return copyboard
    



def get_iterator(board):
    """
    Paradeigma:

    >>> game = board(3)
    >>> set_alive(game, (2, 1), True)
    >>> for cell in get_iterator(game):
    ...     print(cell)
    ... 
    ((0, 0), False)
    ((0, 1), False)
    ((0, 2), False)
    ((1, 0), False)
    ((1, 1), False)
    ((1, 2), False)
    ((2, 0), False)
    ((2, 1), True)
    ((2, 2), False)
    """
    
    list=board.items()
    return list


def print_board(board):
    """

    >>> game = board(5)
    >>> set_alive(game, (0,0), True)
    >>> set_alive(game, (2,2), True)
    >>> set_alive(game, (4,4), True)
    >>> set_alive(game, (3,4), True)
    >>> set_alive(game, (0,4), True)
    >>> print_board(game)
    ⬛⬜⬜⬜⬛
    ⬜⬜⬜⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬛
    ⬜⬜⬜⬜⬛
    """ 
     
    n=get_size(board)
    table=[]
    for i in range(n):
        table.append([])
        for j in range(n):
            if board[i,j] == True:
                table[i].append(u'\u25FB')
            else:
                table[i].append( u'\u25FC')
    for i in table:
        print(*i)


def neighbors(p):
    """

    >>> neighbors((3,2))
    {(3, 3), (3, 1), (2, 1), (2, 3), (4, 3), (2, 2), (4, 2), (4, 1)}
    >>> neighbors((0,0))
    {(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1)}
    >>> neighbors((0,10))
    {(-1, 9), (1, 10), (-1, 11), (0, 11), (-1, 10), (1, 9), (0, 9), (1, 11)}
    """
    
    neighset=set()
    for i in range(p[0]-1,p[0]+2):
        for j in range(p[1]-1,p[1]+2):
            if (i,j)!=p:
                neighset.add((i,j))
    return neighset

    
def place_blinker(board, p = (0,0)):
    """
    
    >>> game = board(5)
    >>> place_blinker(game)
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (1,2))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (4,4))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬛
    """
    
    for i in range(p[0],p[0]+3):
        set_alive(board,(i,p[1]),True)
    return board




def place_glider(board, p = (0,0)):
    """

    >>> game = board(7)
    >>> place_glider(game)
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    >>> place_glider(game, (3,3))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬜⬛⬜
    ⬜⬜⬜⬜⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜
    """
    
    i=p[0]
    j=p[1]
    place_blinker(board,(i,j+2))
    set_alive(board,(i+1,j),True)
    set_alive(board,(i+2,j+1),True)
    return board


def tick(board):
    """

    >>> game = board(6)
    >>> place_glider(game)
    >>> place_blinker(game, (3,4))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    >>> tick(game)
    >>> print_board(game)
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬛⬛⬛⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬜⬛⬛⬛
    ⬜⬜⬜⬜⬜⬜
    """
    
    length=get_size(board)
    new=copy_board(board)
    help=get_iterator(new)
    for i in help:
        hood=neighbors(i[0])
        alivehood=[]
        for x in hood:
            if x[0]>-1 and x[1]>-1 and x[0]<length and x[1]<length:
                    if new[x]==True:
                        alivehood.append(x)
        if i[1]==False:
            if len(alivehood)==3:
                        set_alive(board,i[0],True)
        else:
            if len(alivehood)<=1 or len(alivehood)>=4:
                        set_alive(board,i[0],False)
            elif len(alivehood)<4:
                        set_alive(board,i[0],True)
    return board 



if __name__ == '__main__':
    game = board(10)
    place_blinker(game, (1,2))
    place_glider(game, (2,4))
    print_board(game)

    from time import sleep
    for i in range(101):
        sleep(3)
        tick(game)    
        print(" ")
        print(" ")
        print_board(game) 
        
        