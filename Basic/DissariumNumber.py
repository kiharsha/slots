def isDissarium(number1):
    digit_sum =0
    for i in range(1, number1):
        num_str = str(i)
        digit_sum = sum(int(i) ** (index+1) for index, i in enumerate(num_str))
        if digit_sum == i:
            print(i)


number = int(input("Enter a number"))
print(isDissarium(number))
