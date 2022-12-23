#03.Задайте список из вещественных чисел.Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19    
import random
flag=1
while flag :
    try:
        numbInterval = input('Укажите интервал для формирования списка вещественных чисел (через пробел)  :').replace(',','.') .split()
        numberItem =abs(int(input('Введите количество элементов  для формирования списка вещественных чисел (больше 0):')))
        numList = [float(i) for i in numbInterval]
        if numList[0] != numList[1]:
            flag=0
        else:
            print('Введены равные значения концов интервала. Повторите ввод ')
    except:    
        print(f'Введена недопустимая комбинация : интервал "{numbInterval}", количество элементов "{numberItem}" ')
        print('Повторите ввод')
list01=[]
if numList[0] > numList[1]:
    numList[0], numList[1] =  numList[1], numList[0]
for i in range(numberItem):
    list01.insert(0,round(random.uniform(numList[0], numList[1]),3))
minFractionalPart =1.0
maxFractionalPart =0.0
for i in range(len(list01)):
    fractionalPart=list01[i]%1.0
    if (fractionalPart<minFractionalPart and fractionalPart!=0.0):
        minFractionalPart=fractionalPart
    if fractionalPart>maxFractionalPart:
        maxFractionalPart=fractionalPart
print(f'Сформированный список вещественных чисел: {list01}')
print(f'Разница между максимальным и минимальным значением дробной части элементов')
print(f'списка равна {round((maxFractionalPart-minFractionalPart),3)}')
