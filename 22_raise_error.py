a = int(input("Enter the number b/w 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("value should be b/w 5 & 9 ")
else:
    print(a)

