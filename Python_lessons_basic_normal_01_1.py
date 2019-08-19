print ('Введите исследуемое число')
a = int(input())
D = 0 
while a>0:
    b = a%10
    if b>D:
        D=b
    a = a//10
print ('Наибольшая цифра =', D)

