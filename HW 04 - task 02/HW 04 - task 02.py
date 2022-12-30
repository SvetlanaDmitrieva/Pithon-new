#02.Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.
def parsing_string(new_str:dict,max_coeff:int):
    for item in new_str:
        max_split = -1
        val_0 = item.split('x',max_split)
        val_1 = val_0[0]
        if max_split == -1 :
            coeff = 0
        if (len(val_0) == 2):
            rest_02 = val_0[1].split('**')
            if len(rest_02) == 1 :
                coeff = 1
            else:
                coeff = int(rest_02[1])
        if val_1.endswith('*') :
            val_1 = val_1[:-1]
        if val_1 == '' :
            val_1 = '1'
        elif val_1 == '-' :
            val_1 = '-1'
        value = int(val_1)
        if coeff > max_coeff :
            max_coeff = coeff
        dict_equatin[coeff] = dict_equatin.get(coeff,0) + value
    return max_coeff

max_coeff = -100000
dict_equatin = {}
list_files = ['file01.txt','file02.txt']
for i in range(2):
    fileS = open((list_files[i]),'r')  #открытие файлов для чтения многочленов
    string_file = str(fileS.readline())
    fileS.close()
    print(f'строка многочлена {i+1} = {string_file}')
    new_string = string_file.replace(' ','').replace('=0','')\
        .replace('+',' ').replace('-',' -').replace('^','**')\
        .replace('х','x').replace('Х','x') .replace('X','x').split()
    max_coeff = parsing_string(new_string,max_coeff)
string_file = ''
for coeff, value in dict_equatin.items() :
    if value != 0:
        strValue = str(value)
        if not strValue[0].startswith('-') and coeff != max_coeff :
            strValue = '+' + strValue
        if coeff > 0 : 
            if value in [-1,1] : 
                strValue = strValue[0] + 'x'
            else:
                strValue += '*x'
        if coeff > 1 :
            strValue += f'**{coeff}'
        string_file += strValue
string_file += '=0\n'
print(f'сумма многочленов = {string_file}') # запись строки суммы многочлена в новый файл
fileS=open('file03.txt','w')
fileS.write(string_file)
fileS.close()