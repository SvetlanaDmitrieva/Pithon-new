#06-03.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 # Т е для k = 8, список будет выглядеть так:
 #  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи 
def n_Fibonacci(numb):
    if numb == 0:
        return 0
    if numb in [-1,1]:
        return 1
    if numb > 1:
        return n_Fibonacci(numb-1) + n_Fibonacci(numb-2)
    if numb < -1:
        return n_Fibonacci(numb+2) - n_Fibonacci(numb+1)
  
    
fib_number = None
while not (type(fib_number) == int ):
    fib_number=abs(int(input('Введите положительное число для  списка Фибоначчи: ')))
list_fibonacci=[n_Fibonacci(numb) for numb in range(-fib_number,fib_number+1)]
print(f'Список Фибоначчи : {list_fibonacci}')
