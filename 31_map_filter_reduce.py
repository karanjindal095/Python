cube = lambda x: x*x*x
l1 = [1,2,4,6,4,3]
l2 = []
for item in l1:
    l2.append(cube(item))
print(l2)

''' 01. map '''
m1 = list(map(cube,l1))
print(m1)

''' 02. filter '''
great = lambda a: a>2
f1 = list(filter(great,l1))
print(f1)

''' 03. reduce '''
from functools import reduce
add = lambda a,b: a+b
num = [1,2,3,4,5]
r1 = reduce(add,num)
print(r1)
sum = 0
for i in num:
    sum = sum + i
print(sum)