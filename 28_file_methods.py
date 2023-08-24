'''01 writelines() '''
f = open("python/file1.txt","w")
l = ["50,","60,","70\n","80,","90,","100\n","110,","120,","130"]
f.writelines(l)
f.close()

'''02 readline() '''
f = open("python/file1.txt","r")
i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])       #50,60,70
    m2 = int(line.split(",")[1])       #80,90,100
    m3 = int(line.split(",")[2])       #110,120,130

    print(f"marks of student {i} in math is   {m1*2}")
    print(f"marks of student {i} in sst is    {m2*2}")
    print(f"marks of student {i} in python is {m3*2}")

    print(line)
f.close()