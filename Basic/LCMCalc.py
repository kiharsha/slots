def lcmcalc(a, b):
    count = 0
    if a > b:
        greater = a
    else:
        greater = b
    while (True):
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        count += 1
        greater += 1
    return lcm, count


a = 54
b = 24
lcm, count = lcmcalc(a, b)
print(f"{lcm}, {count}")
