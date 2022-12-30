#01.Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
degreeNat = int(input('Введите натуральную степень многочлена (положительное, целое) :'))
flag = 1 
equation1 = {}
for i in range (degreeNat, -1, -1):
    if i == degreeNat:
        while flag:             # во избежание нулевого коэффициента для первого элемента 
            equation1[i] = random.randint(-100, 100)
            # print(F' i = {i} , equation1[i] = {equation1[i]}')  
            if equation1[i] != 0:
                flag = 0
    else:
        equation1[i] = random.randint(-100, 100)
        # print(F' i = {i} , equation1[i] = {equation1[i]}') 
eqStr = '' 
for coefficient, value in equation1.items() :
    if value != 0:
        strValue = str(value)
        if strValue[0] !='-' and coefficient != degreeNat:
            strValue = '+' + strValue
        if coefficient > 0 : 
            if value in [-1,1] : 
                strValue = strValue[0] + 'x'
            else:
                strValue += '*x'
        if coefficient > 1 :
            strValue += f'**{coefficient}'
        eqStr += strValue
eqStr += '=0\n'
print(eqStr)
file = open('filePython.txt','a')
file.write(eqStr)
file.close()
