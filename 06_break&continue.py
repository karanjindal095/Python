a = int(input("Enter the number = "))
for i in range(1,15):
    if(i==10):
        break
    if(i==5):
        continue    
    print(a,"*",i,"=",a*i)