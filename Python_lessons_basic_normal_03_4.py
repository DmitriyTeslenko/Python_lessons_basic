import math

#Ручной ввод координат
#coords=[['', '  x', 'y'], ['A1', 0, 0], ['A2', 0, 0], ['A3', 0, 0], ['A4', 0, 0]]
#for i in range (1, 5):
#    for j in range (1, 3):
#        print('Введите координаты точки', coords[i][0], coords[0][j])
#        coords[i][j]=float(input())
#    print()    

#Отладка формирования таблицы
#for i in range (5):
#    for j in range (3):
#        print(coords[i][j], end='  ')
#    print()

# Дополнительная проверка таблицы
#print(coords)

#Отладочный ввод координат         
coords=[['', '  x', 'y'], ['A1', 8.0, 8.0], ['A2', 10.0, 12.0], ['A3', 16.0, 13.0], ['A4', 14.0, 9.0]]

# Преобразование координат в более удобный вид. Это можно и не делать, но мне так нагляднее
A1=list(coords[1][1:3])
A2=list(coords[2][1:3])
A3=list(coords[3][1:3])
A4=list(coords[4][1:3])
#print (A1)
#print (A2)
#print (A3)
#print (A4)

# Считаем параллелограм всегда имеющим наименования точек по порядку, например
# A2 A3
# A1 A4

# Перенос вектора A1-A2 в начало координат
x_A2 = A2[0]-A1[0]
y_A2 = A2[1]-A1[1]
# Перенос вектора A3->A4 в начало координат
x_A3 = A3[0]-A4[0]
y_A3 = A3[1]-A4[1]

# Проверка совпадения точек

if x_A2==x_A3 and y_A2==y_A3:
    print('Точки являются вершинами параллелограмма')
else:
    print('Облом, это не параллелограмм')
