#05-01.Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры 
# человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 
import random

def step_game() :
    global flag, rest, player, game
    flag = flag%2
    player = 0
    if flag == 1 or (flag != 1 and game == 1):
        step_player()
    else:
        step_bot()
    rest -= player
    if rest != 0:
        flag += 1
        print(f' Конфет = {rest}')
    return


def step_player():
    global player
    while True: 
        player = int(input(f'Ход игрока {(pr_flag[flag])} :'))
        if player > 28 or player > rest:
            print (f'Превышено допустимое значение конфет ({min(rest,28)}), повторить ход')
            continue
        else:
            break
    return 


def step_bot():
    global player,rest
    if rest%29 != 0:
        player = rest%29
    else:
        player = random.randint(1,28)
    print(f'Ход бота :{player}')
    return 


pr_flag = {1:1, 0:2}
rest = 0
game = int(input(f'Введите: 1-если хотите играть с человеком, 2-если хотите играть с ботом :'))
while rest < 29:
    rest = int(input(f'Введите начальное количество конфет(больше 28) :'))
flag = random.randint(0,1)+1
while rest > 0:
     step_game()
if flag == 1 or (flag != 1 and game == 1):
    print (f'Выиграл  игрок {pr_flag[flag]}')
else:
    print (f'Выиграл  бот')
