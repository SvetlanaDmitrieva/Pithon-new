#06-02. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
while True :
    try:
        numberList=input('Введите список целых чисел(через пробел):').split()
        list01= list(map(int,numberList))
        break
    except:
        print(f'Введена недопустимая строка целых чисел: "{numberList}"')
        print('Повторите ввод')
middleList01=int(round((len(list01)+0.2)/2,0))
list02=[list01[i]*list01[len(list01)-1-i] for i in range (middleList01)]
print(f'Введенный список чисел :{list01}') 
print(f'Список произведений пар чисел во введенном списке: {list02}')
