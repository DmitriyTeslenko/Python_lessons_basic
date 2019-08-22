import math

def int_sqrt(a):
    return int(math.sqrt(a))

list_1 = [2, -5, 8, 9, -25, 25, 4]
list_2 = []
for i in range (len(list_1)):
    if list_1[i]>=0 and int_sqrt(list_1[i])**2 == list_1[i]:
       list_2.append(int_sqrt(list_1[i]))
print (list_2)

