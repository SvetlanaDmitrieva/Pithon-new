import csv
import shutil

def add_new_contact (new_contact:list):  
    string_inp=''
    string_inp=str(','.join(new_contact))
    return string_inp

def write_new_contact(new_contact):
    with open(r'phone_guide.csv', mode='a',encoding='cp1251') as w_f:
        file_writer=csv.writer(w_f,delimiter=",", dialect='excel',lineterminator= '\r')
        print(f'Строка ввода : {new_contact})')
        file_writer.writerow( new_contact)
    sort_exit()

def get_contact(last_name:str):
    coln=0
    result=[]
    o=open('phone_guide.csv', mode='r')
    file_data=csv.reader(o,delimiter = ",")
    for index,row in enumerate(file_data):
        if row[coln] == last_name:
            print(f'Индекс :{index} : {str(row)}')
            l_ind_row = (index,row)
            result.append(l_ind_row)
    o.close()
    return result
  

def open_file():
    try:
        f=open('phone_guide.csv')
        f.close()
    except FileNotFoundError:
        with open('phone_guide.csv', mode='a',encoding='cp1251') as w_f:
            names = ["Фамилия","Имя","Отчество", "Телефон", "Адрес"]
            file_writer = csv.writer(w_f, delimiter = ",", 
                        lineterminator="\r")
            file_writer.writerow(names)


def delete_contact(index):
    with open('phone_guide.csv','r',newline='') as source,open('phone_guide_n.csv', 'w', newline='') as dest:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(dest,delimiter=',')
        for line,row in enumerate(reader):
            if line == index:
                 continue 
            writer.writerow(row)  
    shutil.copyfile('phone_guide_n.csv','phone_guide.csv')

def change_contact(index:int, new :list):
    with open('phone_guide.csv','r',newline='') as source,open('phone_guide_n.csv', 'w', newline='') as dest:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(dest,delimiter=',')
        for line,row in enumerate(reader):
            if line == index:
                ren_new = renovationin(row, new)
                writer.writerow(ren_new) 
            else:
                writer.writerow(row)  
    shutil.copyfile('phone_guide_n.csv','phone_guide.csv')
    

def renovationin(row, new):
    row[0] = new[0] if new[0] != '' else row[0]
    row[1] = new[1] if new[1] != '' else row[1]
    row[2] = new[2] if new[2] != '' else row[2]
    row[3] = new[3] if new[3] != '' else row[3]
    row[4] = new[4] if new[4] != '' else row[4]
    return row

def sort_exit():
    with open('phone_guide.csv', 'r',encoding='cp1251') as f:
        readit = csv.reader(f,delimiter=',')
        head_file=next(readit)
        thedata = list(readit)
    thedata.sort(key=lambda x: (x[0],x[1],x[2]))
    with open('phone_guide_n.csv', 'w',newline='',encoding='cp1251') as f:
        writeit = csv.writer(f,delimiter=',')
        writeit.writerow(head_file)
        writeit.writerows(thedata)
    shutil.copyfile('phone_guide_n.csv','phone_guide.csv')
    
