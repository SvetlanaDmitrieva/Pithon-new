#01.Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
number = input("Введите вещественное число: ")
number01 = number.replace('-','') 
number01 = number01.replace(',','.') 
try:
      listN=number01.split('.')
      number02=listN[0]+listN[1] 
      sumNumbers=0
      for val in number02:
            sumNumbers+= int(val) 
      print(f'Сумма цифр введенного числа {number} равна = {sumNumbers}')
except:
      print(f'Введена недопустимая комбинация "{number}"')