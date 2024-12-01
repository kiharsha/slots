def addition():
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    sum_result = num1 + num2
    return sum_result

def division():
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        div_result = num1 / num2
    return div_result


sum_result1 = addition()
div_result1 = division()
print(f"sum:  {sum_result1}")
print(f"Division: {div_result1}")


