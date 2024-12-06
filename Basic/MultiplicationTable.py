num = int(input("Enter the number for Multiplication table"))
num1 = int(input("Enter the last number to be multiplied with"))

for i in range(1,num1+1):
    sum = num * i
    print(f"{num} * {i} = {sum}")