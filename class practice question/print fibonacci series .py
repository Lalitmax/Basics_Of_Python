# print fibonacci series
terms=int(input("Enter number of terms : "))

n1,n2=1,2
i=2

if(terms==1):
    print(n1)
elif(terms==2):
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    while(i<terms):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i=i+1
