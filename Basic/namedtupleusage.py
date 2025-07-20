"""NamedTuples provide a way to create tuple like objects with named fields"""
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p1=Point(3,4)
p2=Point(x=4,y=2)
print(f"Point 1 x={p1.x},y={p1.y}")
print(f"Point 2 x={p2.x},y={p2.y}")
print(f"Point 1{p1[0]},{p1[1]}")
Employee=namedtuple('Employee','name age jobtitle')
emp1=Employee('Alice',30,'Engineer')
print(emp1.name)
Person=namedtuple('Person',['first_name','last_name'])
data=['John', 'Doe']
person_from_list=Person._make(data)
print(f"list:{person_from_list.first_name}")