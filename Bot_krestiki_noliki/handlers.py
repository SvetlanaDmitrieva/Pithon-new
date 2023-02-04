import random

from aiogram import types
from loader import dp

LIST_SYMBOL=['X','O']
BOARD_SIZE=9
VOID=' '
DRAW='Ничья'
num_step = 0
step = 0
view_step = LIST_SYMBOL[num_step]
new_game = False
board = []


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name}, привет! Сегодня сыграем с тобой в крестики-нолики! Для начала игры введи команду /new_game. '
                          f'Чтобы сделать ход игроку, нужно ввести номер клетки,\n'
                         f'куда хочешь поставить свой символ. Бот ставит свой ход сам:\n'
                         f'    0 | 1 | 2 \n'
                         f'    --------- \n'
                         f'    3 | 4 | 5 \n'
                         f'    --------- \n'
                         f'    6 | 7 | 8 \n')


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global LIST_SYMBOL
    global human
    global bot
    global board
    global new_game
    global step
    board.clear()
    name = message.from_user.first_name
    new_game = True
    first = random.randint(0,1)
    bot = LIST_SYMBOL[1] if first else LIST_SYMBOL[0]
    human = LIST_SYMBOL[0] if first else LIST_SYMBOL[1]
    if first:
        await message.answer(f'Игра началась. По жребию первым ходит {name}! Ход игрока (номер клетки (0-8)...')
    else:
        await message.answer(f'Игра началась. По жребию первым ходит Ботяо')
    new_board()
    await display_board(message)
    if not first:
        await bot_turn(message)
        board[step] = bot
        await before_step(message)
        await message.answer(f'{name}, продолжай. Твой ход')


@dp.message_handler()
async def mes_human_step(message: types.Message):
    global new_game
    global board
    global human
    global bot
    global step
    name = message.from_user.first_name
    free_moves = []
    free_moves = available_moves(board)
    if not message.text.isdigit():
        await message.answer (f'{name},некорректный ход, надо указать ЧИСЛО от 0 до 8!')
    else:
        step = int(message.text)
        if step in free_moves:
            board[step] = human
            await before_step(message)
            if new_game == True :
                await bot_turn(message)
                board[step] = bot
                await before_step(message)
        else:
            await message.answer (f'{name},некорректный ход, надо указать свободную ячейку от 0 до 8!')
        
    if new_game == True :
        await message.answer(f'{name}, продолжай. Твой ход')


def new_board():
    global board
    global BOARD_SIZE
    global VOID
    for _ in range(BOARD_SIZE):
        board.append(VOID)
    return 


async def display_board(message:types.Message ):
    global board
    await message.answer(f'--------------\n'
                        f'| {board[0]} | {board[1]} | {board[2]} |\n'
                        f'--------------\n'
                        f'| {board[3]} | {board[4]} | {board[5]} |\n'
                        f'--------------\n'
                        f'| {board[6]} | {board[7]} | {board[8]} |\n'
                        f'--------------\n')


async def before_step(message:types.Message ):
    global view_step
    global board
    global num_step
    global new_game
    global LIST_SYMBOL
    global bot
    global human
    global DRAW
    await display_board(message)
    num_step += 1
    view_step = LIST_SYMBOL[num_step%2]
    if winner(board):
        winner_name = winner(board)
        await congratulations_winner(message, winner_name,bot,human)
        new_game = False


async def congratulations_winner(message: types.Message, winner_game,bot,human):
    global board
    if winner_game != DRAW:
        await message.answer(f'Победа! {winner_game}')
    else:
        await message.answer(f'{DRAW}')
    if winner_game == bot:
        await message.answer('Бот выиграл!')
    elif winner_game == human:
        name = message.from_user.first_name
        await message.answer(f'{name}! Ты победил!')

    
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


def available_moves(board_r:list):
    global BOARD_SIZE
    global VOID
    free_moves = []
    for i in range(BOARD_SIZE):
        if board_r[i] == VOID:
            free_moves.append(i)
    return free_moves


def check_second_step_bot(board, k):
    if  (board[0] == board[8] == 'X') or \
        (board[2] == board[6] == 'X'):
        return 1
    else:
        return k

async def bot_turn(message: types.Message):        
    global board
    global bot 
    global human 
    global num_step
    global new_game
    global VOID
    global step 
    board_copy = board[:]
    BEST_STEPS = (4,0,8,2,6,1,3,5,7)
    bot_step = 'БОТ:Мой ход: '
    for j in available_moves(board):
        board_copy[j] = human
        if winner(board_copy) == human:
            await message.answer(f'{bot_step},{j}')
            step = j 
            return
        board_copy[j] = VOID
    best_line = [x for x in BEST_STEPS if x in available_moves(board)]
    for i in best_line:
        board_copy[i] = bot
        if winner(board_copy) == bot:
            await message.answer(f'{bot_step},{i}') 
            step = i 
            return 
        board_copy[i] = VOID
    for k in best_line:
        if num_step == 3 and bot == 'O':
            k = check_second_step_bot(board,k)
        await message.answer(f'{bot_step},{k}') 
        step = k
        return 
