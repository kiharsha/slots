def RemEmptyList(numberslt):
    for i in numberslt:
        if len(i) == 0:
            numberslt.remove(i)
    return numberslt


def clonelst(numberlst):
    clonelst = list(numberlst)
    print(clonelst)


def occurence(numberlist, k):
    count = 0
    for i in numberlist:
        if i == k:
            count += 1
    return count


def removeithcharacter(charlistt, k):
    count = 0
    for i in charlistt:
        if count == k - 1:
            charlistt.remove(i)
        count += 1
    return charlistt


def removeithcharacterr(charlistt, i):
    if i < 0 or i >= len(charlistt):
        print(f"Invalid index {i}. The string remains unchanged")
        return charlistt
    result_str = charlistt[:i] + charlistt[i + 1:]
    return result_str


numberslst = [[5, 6, 7], [], [1, 2, 3], [], [9, 8, 7]]
numberlist = [9, 4, 5, 7, 15, 11, 12, 12, -1, -3, -5, 4]
print(RemEmptyList(numberslst))
clonelst(numberslst)
print(occurence(numberlist, 4))
listchar = ['t', 'y', 'p', 'e', 'u', 'q', 'n', 'l', 'm']
print(removeithcharacterr(listchar, 4))
