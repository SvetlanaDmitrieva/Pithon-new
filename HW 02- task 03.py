#03.Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ
# SHUFFLE, максимум использование библиотеки Random для получения случайного int 
import random

flag=1
while flag :
    try:
        setNumbers00=input('Введите количество элементов списка (больше 0):')
        setNumbers=abs(int(setNumbers00))
        if setNumbers != 0:
            flag=0
        else:
            print('Введено число 0.Повторите ввод')
    except:    
        print(f'Введена недопустимая комбинация :"{setNumbers00}"')
        print('Повторите ввод')
listNumbers01=[]
listNumbers02=[]
for i in range(setNumbers):
    listNumbers01.insert(0,random.randint(-setNumbers, setNumbers))
    listNumbers02.insert(0,listNumbers01[0])
for i in range(setNumbers-1, 0, -1):
    j = random.randint(0, i + 1) 
    listNumbers02[i], listNumbers02[j] = listNumbers02[j], listNumbers02[i] 
print (f"Исходный список : {listNumbers01}")
print (f"Перемешанный список : {listNumbers02}")