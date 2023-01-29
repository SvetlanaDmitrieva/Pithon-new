import model 
import view

def start():
    choice = ''
    while True:
        choice = view.main_menu()
        match choice:
            case 1 :
                model.open_file()
                view.information('\nФайл успешно открыт\n')
            case 2:
                view.show_contacts()
            case 3:
                new_contact = list(view.create_new_contact())
                new_contact_input = model.add_new_contact(new_contact)
                view.information_data(new_contact_input)
                yes_now=int(input(view.information('Подтвердите ввод (1- записать, 2- отмена ввода) :')))
                if(yes_now == 1):
                    model.write_new_contact(new_contact)
                    view.information(f'\nКонтакт {new_contact} успешно создан\n')
            case 4:
                del_name = view.select_contact('Введите фамилию удаляемого контакта: ')
                contact_ind = model.get_contact(del_name)
                if contact_ind != []:
                    index = 0
                    if len(contact_ind) > 1:
                        index = view.number_index(contact_ind)
                    else:
                        index = int(contact_ind[0][0])
                    if not index :
                            break
                    confirm = view.delete_confirm(contact_ind,index)
                    if confirm :
                        model.delete_contact(index)
                        view.information(f'\nКонтакт с индексом {index} успешно удален\n')
                else:
                    view.empty_request()
            case 5 :
                name = view.select_contact('Введите фамилию изменяемого контакта: ')
                contact_ind = model.get_contact(name)
                if contact_ind != [] :
                    index = 0
                    if len(contact_ind) > 1:
                        index = view.number_index(contact_ind)
                    else:
                        index = int(contact_ind[0][0])
                    if not index :
                            break
                    changed_contact = view.change_contact()
                    model.change_contact(index, list(changed_contact))
                    view.information(f'\nКонтакт с индексом {index} успешно изменен\n')
                else:
                    view.empty_request()
            case 6 :
                find = view.find_contact()
                result = model.get_contact(find)
                if len(result) < 1:
                    view.information('Указанный контакт не найден')
            case 7 :
                view.end_program()
                model.sort_exit()
                break
            case _ :
                view.input_error()