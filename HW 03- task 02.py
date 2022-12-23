#02. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
flag=1
while flag :
    try:
        numberList=input('Введите список целых чисел(через пробел):').split()
        list01= list(map(int,numberList))
        flag=0
    except:
        print(f'Введена недопустимая строка целых чисел: "{numberList}"')
        print('Повторите ввод')
list02=[]
lenList01=len(list01)
middleList01=lenList01//2
for i in range(middleList01):
    list02.append(list01[i]*list01[lenList01-1-i])
if (lenList01%2!=0):
    list02.append(list01[middleList01]**2)
print(f'Введенный список чисел :{list01}') 
print(f'Список произведений пар чисел во введенном списке: {list02}')
