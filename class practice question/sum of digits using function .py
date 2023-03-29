def sumofdigits(n):

    sum=0
    while(n>0):
        sum=sum+n%10
        n //=10
    return sum

n=int(input("Enter digits : "))

print("sum of digits is ",sumofdigits(n))