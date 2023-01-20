#05-02.Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
#  Добавить игру против бота с интеллектом.

LIST_SYMBOL=['X','O']
BOARD_SIZE=9
VOID=' '
DRAW='Ничья'

def manual():
    print('''
Это игра "Крестики-нолики" с ботом.
Чтобы сделать ход игроку, нужно ввести номер клетки,
куда хочешь поставить свой символ. Бот ставит свой ход сам:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
''')
def start(question):
    answer = None
    while answer not in (0,1):
        answer = int(input(question).lower())
    return answer


def first_step():
    answer_01=['Первым ходит Игрок: ','Первый ход делает Бот']
    question = start("Вы хотите играть первым - 0, вторым - 1? ")
    print(f'{answer_01[question]}')
    human = LIST_SYMBOL[question]
    bot = LIST_SYMBOL[(question+1)%2]
    return bot, human


def step_number(low,high):
    answer = None
    while answer not in range(low,high):
        answer = int(input("Ход игрока (номер клетки (0-8)): "))
    return answer


def new_board():
    board = []
    for i in range(BOARD_SIZE):
        board.append(VOID)
    return board


def display_board(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
    

def available_moves(board):
    free_moves = []
    for i in range(BOARD_SIZE):
        if board[i] == VOID:
            free_moves.append(i)
    return free_moves


def winner(board):
    VAR_WIN = ((0,4,8), (2,4,6),(0,1,2), (3,4,5), 
               (6,7,8), (0,3,6),(1,4,7), (2,5,8), )
    for i in VAR_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != VOID:
            winner = board[i[0]]
            return winner
        if VOID not in board:
            return DRAW
    return None


def human_step(board):
    free_moves = available_moves(board)
    step = None
    while step not in free_moves:
        step = step_number(0,BOARD_SIZE)
        if step not in free_moves:
            print('Некорректный ход. Напиши другой номер: ')
    print('Ок!')
    return step


def check_second_step_bot(board, k):
    if  (board[0] == board[8] == 'X') or \
        (board[2] == board[6] == 'X'):
        return 1
    else:
        return k

def comp_step(board,bot,human, number_step):
    board_copy = board[:]
    BEST_STEPS = (4,0,8,2,6,1,3,5,7)
    bot_step = 'БОТ:Мой ход: '
    for j in available_moves(board_copy):
        board_copy[j] = human
        if winner(board_copy) == human:
            print(bot_step,j)
            return j
        board_copy[j] = VOID
    best_line=[x for x in BEST_STEPS if x in available_moves(board_copy)]
    for i in best_line:
        board_copy[i] = bot
        if winner(board_copy) == bot:
            print(bot_step,i)
            return i
        board_copy[i] = VOID
    for k in best_line:
        if number_step == 3 and bot == 'O':
            k = check_second_step_bot(board,k)
        print(bot_step,k)
        return k


def congratulations_winner(winner_game,bot,human):
    if winner_game != DRAW:
        print('Победа! ', winner_game)
    else:
        print(DRAW)
    if winner_game == bot:
        print('Бот выиграл!')
    elif winner_game == human:
        print('Ты победил!')
        
def main():
    manual()
    bot,human = first_step()
    num_step = 0
    view_step = LIST_SYMBOL[num_step]
    board = new_board()
    display_board(board)
    while not winner(board):
        if view_step == human:
            step = human_step(board)
            board[step] = human
        else:
            step = comp_step(board,bot,human,num_step)
            board[step] = bot
        display_board(board)
        num_step += 1
        view_step = LIST_SYMBOL[num_step%2]
    winner_game = winner(board)
    congratulations_winner(winner_game,bot,human)

main()
input('\n Нажми Enter, чтобы выйти')