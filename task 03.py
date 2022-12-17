#3.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
coordinateX= float(input('Введите Х координату: '))
coordinateY= float(input('Введите Y координату: '))
if coordinateX == 0.0 :
    if coordinateY == 0.0:
        print('Точка находится в начале координат') 
    else:
        print('Точка находится на оси Y')
else:
    if coordinateY == 0.0:
        print('Точка находится на оси X') 
    else:
        if coordinateX > 0.0 and coordinateY > 0.0:
            print('Точка находится в первой четверти координатной плоскости') 
        elif coordinateX > 0.0 and coordinateY < 0.0:
            print('Точка находится в четвертой четверти координатной плоскости')
        elif coordinateX < 0.0 and coordinateY > 0.0:
            print('Точка находится в второй четверти координатной плоскости')
        else:                    # coordinateX < 0.0 and coordinateY < 0.0:
            print('Точка находится в третьей четверти координатной плоскости')