def cube1(a):
    return a*a*a
print(cube1(5))

''' lambda function'''
cube = lambda a: a*a*a
double = lambda x: x*2
avg = lambda x,y,z: (x+y+z)/3

print(cube(2))
print(double(3))
print(avg(5,10,15))

def appl(fx,value):
    return 6 + fx(value)
print(appl(cube,2))           #passed function as an argument
print(appl(lambda x: x*x,2))  #passes function without its name (anonymous function)