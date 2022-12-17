#5.Найти расстояние между двумя точками пространства
size=int(input('Введите размерность пространства(2- двухмерное, 3- трехмерное): '))
#создание массива координат точек
coordinates=[0.0]*2
for i in range (2):
    coordinates[i]=[0.0]*size
#ввод координат 
sum=0.0
for i in range(2):
    for j in range(size):
        coordinates[i][j]=float(input(f'Введите {j+1} координату  {i+1} точки: '))
for j  in range (size):
    sum+=(coordinates[0][j]-coordinates[1][j])**2
distance2points=sum**0.5
print(f'Расстояние между двумя точками равно {distance2points}')
