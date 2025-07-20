def testreverse(a):
    print(a)
    if len(a) == 0:
        return a
    else:
        return testreverse(a[1:]) + a[0]


result = testreverse("reversal")
print(result)