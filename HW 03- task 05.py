#03-05.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 # Т е для k = 8, список будет выглядеть так:
 #  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи 
def listFibonacci(numb):
    numbersFibonacci= []
    numberA, numberB = 1, 1
    for i in range(numb-1):
        numbersFibonacci.append(numberA)
        numberA, numberB = numberB, numberA + numberB
    numberA, numberB = 0, 1
    for i in range (numb):
        numbersFibonacci.insert(0, numberA)
        numberA, numberB = numberB, numberA - numberB
    return numbersFibonacci
flag=1
while flag :
    try:
        number=input('Введите число для составления списка Фибоначчи: ')
        # вынужденная мера, иначе есди введено НЕ число, в 24 строке ошибка
        number00=abs(int(float(number))) + 1
        # добавили 1, иначе не выполняется условие задачи (для 8)
        flag=0
    except:
        print(f'Введено недопустимое значение: "{number}".Повторите ввод ')   
numbersFibonacci = listFibonacci(number00)
print(f'Список Фибоначчи : {numbersFibonacci}')