def swapwithtempvar():
    a = input("Enter the value of the first variable (a):")
    b = input("Enter the value of the first variable (b):")
    print(f"Original values : a= {a} and b= {b}")
    temp = a
    a = b
    b = temp
    print(f"swap values : a= {a} and b= {b}")


#without temp variable
def swapwithouttemp():
    a1 = input("Enter the value of the first variable (a):")
    b1 = input("Enter the value of the first variable (b):")
    a1,b1=b1,a1
    print(f"Original values : a= {a1} and b= {b1}")


swapwithtempvar()
swapwithouttemp()
