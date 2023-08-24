# 01. reading a file
f = open('python/myfile27.txt','r')
# print(f)
text = f.read()
print(text)
f.close()

# 02. creating a file 
f = open("python/file1.txt","w")
f.close()

# 03. writing in a file
f = open("python/myfile27.txt","w")
f.write("hello karan jindal")
f.close()

# 04. with statement
with open("python/myfile27.txt","a") as f:
    f.write("\nhey i am inside with")