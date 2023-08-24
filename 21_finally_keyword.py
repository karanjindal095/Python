def fun():
    try:
        l = [1,2,5,9,8]
        a = int(input("enter the index :"))
        print(l[a])
        return 1
    except:
        print("error occurred")
        return 0

    finally:
        print("finally executed")

    print("executed")
    
x = fun()
print(x)