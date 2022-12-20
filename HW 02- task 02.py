#02.Задать список из n чисел последовательности (1+1/n)**n и вывести его
# на экран, а так же сумму элементов списка.
def sequenceF (num):
    if num<=0 :
        return print(f'Ошибка ввода: {num} - число не может быть меньше или равно 0')
    else:
        return round((1+1/num)**num, 3)
flag=1
while flag :
    try:
        sequenceNumber00=input('Введите число - длину числовой посдедовательности (1+1/n)**n :')
        sequenceNumber=int(sequenceNumber00)
        flag=0
    except:    
        print(f'Введена недопустимая комбинация :"{sequenceNumber00}"')
        print('Повторите ввод')
listSequence=[]
summSequence=0.0
if sequenceNumber>0 :
    for i in range(sequenceNumber):
        listSequence.append(sequenceF(i+1))
        summSequence+=listSequence[i]
    print(f'Список из {sequenceNumber} чисел последовательности: {listSequence}') 
    print (f'Сумма чисел полученной последовательности : {summSequence}')
else:
    sequenceF(sequenceNumber)
