import random


# Для простоты отладки взял генератор случайных списков из прошлого задания
n=8
list=[]
for i in range (n):
    list.append(random.randint(1, 9))

print(list)

list_2=[]
list_3=[]
# генерация списка неповторяющихся элементов списка 2:
for i in range(len(list)):
    if list_2.count(list[i])==0:
        list_2.append(list[i])
print(list_2)        
# генерация списка с элементами первого списка, не имеющими повторений:

for i in range(len(list)):
    if list.count(list[i])==1:
        list_3.append(list[i])
print(list_3)
