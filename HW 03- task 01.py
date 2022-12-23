#01.Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
import random
flag=1
while flag :
    try:
        numbInterval =input('Укажите интервал для формирования списка случайных чисел (через пробел)  :').split()
        numberItem =abs(int(input('Введите количество элементов  для формирования списка случайных чисел (больше 0):')))
        numList = [int(i) for i in numbInterval]
        if numList[0] != numList[1]:
            flag=0
        else:
            print('Введены равные значения концов интервала. Повторите ввод ')
    except:    
        print(f'Введена недопустимая комбинация : интервал "{numbInterval}", количество элементов "{numberItem}" ')
        print('Повторите ввод')
listNumbers=[]
if numList[0] > numList[1]:
    numList[0], numList[1] =  numList[1],numList[0]
for i in range(numberItem):
    listNumbers.insert(0,round(random.uniform(numList[0], numList[1]),3))
sumNumbers=0.0
for i in range(1,len(listNumbers),2):
    sumNumbers+=listNumbers[i]
print(f'Полученный список чисел : {listNumbers}')   
print(f'Сумма чисел, стоящих на нечетной позиции, равна :{sumNumbers}')