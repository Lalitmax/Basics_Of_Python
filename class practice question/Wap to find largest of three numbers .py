a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a>b):
    if(a>c):        
         print("Largest number is ",a)
    else:
        print("Largest number is ",c)
else :
    if(b>c):
        print("Largest number is ",b)
    else:
        print("Largest number is ",c)