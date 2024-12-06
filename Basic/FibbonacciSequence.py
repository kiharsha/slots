num = int(input("Enter the last number to generate the Fibb Sequence"))
a = 1
b = 1

FibbSequence = a + b
print(f"{a}, {b},{FibbSequence}, ")
b = FibbSequence
c= 1
for i in range(2,num+1):
    FibbSequence1 = c + b
    print(f"{FibbSequence1}")
    c = b
    b = FibbSequence1
