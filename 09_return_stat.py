def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum/len(number)
         
c = average(4,5,6)
print(c)