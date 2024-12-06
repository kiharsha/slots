def HCFCalc(x,y1):

    global hcf
    if x < y1:
        smaller = x
    else:
        smaller = y1
    for i in range(1, smaller+1):
        if (x % i == 0) and (y1 % i == 0):
            hcf = i
    return hcf


x = int(input("Enter first number"))
y1 = int(input("Enter second number"))
c = HCFCalc(x,y1)
print(c)