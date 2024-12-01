num = int(input("Enter a number to calculate factorial"))
factorial = 1
if num == 0:
    print(f"Factorial of {num} is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
        print(factorial)
    print(f"Factorial of {num} is {factorial}")


