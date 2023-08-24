#factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number: "))
print(fact(n))

#febonacii series
def feb(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return feb(num-1)+feb(num-2)
    
num = int(input("Enter the number: "))
for i in range(num):
    print(feb(i))