import os
print('    Меню: \n 1. Перейти в папку \n 2. Просмотреть содержимое текущей папки \n'
      ' 3. Удалить папку \n 4. Создать папку \n Введите номер пункта от 1 до 4 и нажмите Enter')

choise = int(input('     '))

if choise==1:
    dir_0=input('Введите имя директории для перехода      ')
    try:
        os.chdir(dir_0)
        print (os.getcwd() )
    except FileNotFoundError:
        print ('Директории с таким названием нет')
    
elif choise==2:
    print (os.listdir())
elif choise==3:
    dir_0=input('Введите имя директории      ')

    if int(input('подтвердите удаление, введя 1   '))==1:
        try:
            os.rmdir(dir_0)
            print ('Директория удалена')
        except FileNotFoundError:
            print ('Директория с таким названием в папке отсутствует')
elif choise==4:
    dir_0=input('Введите имя создаваемой директории      ')
    try:
        os.mkdir(dir_0)
        print ('Директория создана')
    except FileExistsError:
        print ('Директория с таким названием уже есть')
else:
    print('Нет такой команды')
