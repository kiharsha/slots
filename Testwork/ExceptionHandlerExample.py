def TestExample():
    with open('abc.txt', 'r') as file:
        Lines = file.readlines()
        print(len(Lines))

    for l in Lines:
        print(l)


TestExample()
