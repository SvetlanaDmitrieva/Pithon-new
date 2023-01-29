import pandas as pd

commands = ['Открыть файл',
            "Показать все контакты",
            "Создать контакт",
            "Удалить контакт",
            "Изменить контакт",
            "Найти контакт",
            "Выход из программы"]
def main_menu() :
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choice = ''
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 8:
                return choice
        except ValueError:
            print('Введите корректное значение :')


def show_contacts():
    o=open('phone_guide.csv', mode='r')
    o.close()
    data = pd.read_csv('phone_guide.csv',delimiter=',',encoding='cp1251')
    print(data)
    return

def number_index(contact_ind:list):
    list_index = []
    for  index,row in contact_ind:
        list_index.append(index)
    count = 0
    while True:
        if count == 3: 
            return None
        row_index = (int(input('Введите индекс ИСКОМОГО контакта :'))) 
        if row_index in list_index:
            return row_index
        else:
            print(f'Введен некорректный индекс{row_index}')
            count +=1
       

def input_error():
    print('Ошибка ввода. Введите корректный пунлт меню')

def empty_request():
    print('Искомый контакт не найден')

def show_find_contact(contact_dic):
    for  index,row in contact_dic:
        print(f' Индекс = {index}, контакт : {row}')

def end_program(): 
    print('До свидания. Программа завершена.')

def create_new_contact():
    last_name = input('Введите фамилию :')
    name = input('Введите имя :')
    patronymic = input('Введите отчество :')
    phone = input('Введите телефон:')
    comment = input('Введите адрес:')
    return  last_name, name, patronymic, phone, comment


def find_contact():
    find = input('Введите  фамилию искомого элемента :')
    return find


def delete_contact():
    delete = input('Введите удаляемый контакт')
    return delete


def delete_confirm(contact_ind:list,index:int):
    if index == None :
        return False    
    for ind, row in contact_ind:
        if ind == index:
            result = input(f'Вы действительно хотите удалить контакт {row} ? (y/n)').lower()
            break
    if result == 'н' or result == 'y':
        return True
    else:
        return False

def select_contact(message:str):
    contact = input(message)
    return contact


def change_contact():
    print('Введите новые данные (если изменения не требуютя, нажмите Enter')
    last_name = input('Введите фамилию :')
    name = input('Введите имя :')
    patronymic = input('Введите отчество :')
    phone = input('Введите телефон:')
    comment = input('Введите адрес:')
    return  last_name, name, patronymic, phone, comment
 

def information(text:str):
    print(text)


def information_data(text:str):
    print(f'Введены данные :{text}')

