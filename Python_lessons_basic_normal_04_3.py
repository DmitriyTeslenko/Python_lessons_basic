import random

f = open('2500_figures_numer.txt', 'w')
i=0
while i<2500:
    a=random.randint(0,9)
    f.write(str(a))
    i=i+1
f.close()

f = open('2500_figures_numer.txt', 'r')
str=f.read()
max=0
list_1=[]

for i in range (len(str)-1):
    if str[i+1]==str[i]:
        list_1.append(str[i])
        
        if len(list_1)>max:
            max=len(list_1)
            a=str[i]
    else:
        list_1=[]
        
print(a*(max+1))
f.close()
