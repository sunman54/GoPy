def create_table(size, table):
    x = 1
    for i in range(size):
        table.append([])
        for j in range(size):
            table[-1].append(str(x))
            x+=1
    return table

def player1(table):
    play_to = int(input('Player 1 turn--> '))-1
    size = len(table)
    x = (play_to) % size
    y = (play_to) // size
    if table[y][x] == 'X':
        print('You have made this choise before')
    elif table[y][x] == 'O':
        print('The other player select this cell before')
    else:
        table[y][x] = 'X'

def player2(table):
    play_to = int(input('Player 2 turn--> '))-1
    size = len(table)
    x = (play_to) % size
    y = (play_to) // size
    if table[y][x] == 'O':
        print('You have made this choise before')
    elif table[y][x] == 'X':
        print('The other player select this cell before')
    else:
        table[y][x] = 'Y'

def print_table(table):
    for i in table:
        print('\t'.join(i))
    print('\n')

def check_win(table):
    #check verticaly
    for i in table:
        if len(set(i)) == 1 and i[0] == 'X':
            print('Winner: X')
            return True
        elif len(set(i)) == 1 and i[0] == 'O':
            print('Winner: O')
            return True


    #check horizontaly
    for i in range(len(table)):
        horizol_list = []
        for j in table:
            horizol_list.append(j[i])
        #print(horizol_list)
        if len(set(horizol_list)) == 1 and horizol_list[0] == 'X':
            print('Winner: X')
            return True
        elif len(set(horizol_list)) == 1 and horizol_list[0] == 'O':
            print('Winner: O')
            return True

    # check diagonally
    a = 0
    diagonal_list = []
    while a < len(table):
        diagonal_list.append(table[a][a])
        a+=1
    if len(set(diagonal_list)) == 1 and diagonal_list[0] == 'X':
        print('Winner: X')
        return True
    elif len(set(diagonal_list)) == 1 and diagonal_list[0] == 'O':
        print('Winner: O')
        return True


    b = 0
    c = 2
    diagonal_list = []
    while b < len(table):
        diagonal_list.append(table[c][b])
        b +=1
        c -=1

    if len(set(diagonal_list)) == 1 and diagonal_list[0] == 'X':
        print('Winner: X')
        return True
    elif len(set(diagonal_list)) == 1 and diagonal_list[0] == 'O':
        print('Winner: O')
        return True

    return False






size = int(input('What Size Game GoPY?'))
game_table=create_table(size, [])
print_table(game_table)

while True:
    player1(game_table)
    print_table(game_table)
    if check_win(game_table):break
    player2(game_table)
    print_table(game_table)
    if check_win(game_table):break
