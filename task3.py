# найти наибольший простой делитель числа

n = int(input('Введите число: '))
nums=[]
for i in range(n, 1, -1):
    if(n % i == 0):
        count = 0
        for j in range(2,i+1):
            if(i%j ==0):
                count +=1
        if(count == 1):
            nums.append(i)
maxDenominator = max(nums)
print("Наибольший простой делитель:", maxDenominator)