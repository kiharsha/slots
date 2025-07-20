"""Counting elements in a list"""
from collections import Counter
mylist =['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts=Counter(mylist)
print(counts)
print(type(counts))
mylist1=Counter(['a','b'])
mylist2=Counter(['a', 'b', 'c', 'd', 'a', 'd'])
print(mylist2['a'])
print(counts.most_common(2))
sum_counts=mylist1+mylist2
print(sum_counts)
