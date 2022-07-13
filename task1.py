# найти факториал числа
n = int(input('Введите число: '))
def fact(n): 
    if(n==1 or n==0): 
        return 1 
    else: 
        return n*fact(n-1) 
print("Факториал ",n," равен - ",fact(n))
