a=input("Enter your name : ")
b=''
for i in range(len(a)):
    b= b+a[-i-1]

print(b)