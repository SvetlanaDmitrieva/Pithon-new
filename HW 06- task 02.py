#06-02.Задать список из n чисел последовательности (1+1/n)**n и вывести его
# на экран, а так же сумму элементов списка.
sequenceNumber = -1        
while not (sequenceNumber > 0 and type(sequenceNumber) == int ):
    sequenceNumber=int(input('Введите число - длину числовой посдедовательности (1+1/n)**n :'))
listSequence = [round((1+1/num)**num, 3) for num in range(1,sequenceNumber+1)]
buf = 0
summSequence = [buf := buf + num for num in listSequence]
print(f'Список из {sequenceNumber} чисел последовательности: {listSequence}') 
print (f'Сумма чисел полученной последовательности : {buf}')