def secondlargest(numbers):
    numbers.sort(reverse=True)
    if len(numbers) >= 2:
        second_largest = numbers[1]
        print(second_largest)
    else:
        print("the list does not contain a second largest number")



def NLargestElements(numbers, n):
    sorted_list = sorted(numbers, reverse=True)
    largest_elements = sorted_list[:n]
    return largest_elements


def printEvennum(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)


def printOddnum(numbers):
    for i in numbers:
        if i % 2 != 0:
            print(i)
            

numbers = [6,8,3,10,1,12,11]
secondlargest(numbers)
large_list = NLargestElements(numbers,3)
print(large_list)
printEvennum(numbers)



