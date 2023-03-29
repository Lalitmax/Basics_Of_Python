def count(n):
    cnt=0
    while(n>0):
        n=n//10
        cnt=cnt+1
    return cnt


n=int(input("Enter the numbers : "))
print("no of digits is ",count(n))