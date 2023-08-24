''' is vs == '''
# Both are comparision operator
# ' is ' compare exact location of object in memory
# ' == ' compare values
# for immutable object " is " returns true

a = 4
b = "4"
print(a is b)
print(a == b,"\n") 

x = [1,2,3]
y = [1,2,3]
print(x is y)       #false because list is mutable
print(x == y,"\n")       #true both are equal

l = 3
m = 3
print(l is m)  
'''true because 3 is constant ,here l and m is pointing 
to the same memory location where 3 is stored'''
print(l == m,"\n")

k = (1,2,3)
j = (1,2,3)
print(k is j)
print(k == j )