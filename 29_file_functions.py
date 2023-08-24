'''01 truncate() '''
with open("python/file1.txt","w") as f:
    f.write("1234567890karan9876543210")
    f.truncate(20)

'''02 seek() & tell() '''
with open("python/file1.txt","r") as f:
    line = f.read()
    print(line)
    f.seek(10)
    line2 = f.tell()
    print(line2)
    line3 = f.read(5)
    print(line3)

