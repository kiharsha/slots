def posneg():
    num = float(input("Enter a number"))
    if num > 0:
        print("positive number")
    elif num == 0:
        print("zero")
    else:
        print("Negative number")


def oddoreven():
    a = int(input("Enter a number"))
    if a%2 == 0:
        print("Even number")
    else:
        print("Odd Number")


oddoreven()
posneg()

