flag = False
lower = 1
upper = 10
for num in range(lower,upper+1):
    for i in range(2,num):
        if (num % i) == 0:
            break
        else:
            print(num)



