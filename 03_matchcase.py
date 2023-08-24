a = int(input("Enter the number = "))
match a:
    case 0:
        print("zero")
    case _ if(a<=10):
        print("under 10")
    case _ if(a!=80):
        print("not equal")
    case _:
        print("out")
    