#04. Написать программу преобразования десятичного числа в двоичное .(положительное целое)  
flag=1
while flag :
    try:
        numberDecimal00=input('Введите целое положительное число для перевода в двоичную систему исчисления: ')
        # вынужденная мера, иначе есди введено НЕ число, в 11 строке ошибка
        numberDecimal=abs(int(numberDecimal00))
        flag=0
    except:
        print(f'Введено недопустимое значение: "{numberDecimal00}".Повторите ввод ')
rest=numberDecimal
numberBinary=""
while (rest>0):
     numberBinary=str(rest%2) + numberBinary
     rest//=2
print(f'Десятичное число {numberDecimal} в двоичной системе исчисления равно {numberBinary} ')