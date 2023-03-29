def sum_of_digits(n):
    if n//10==0:
        return n
    else:
        return n%10 + sum_of_digits(n//10)

n=int(input("Enter digits :"))
print("sum of digits = ",sum_of_digits(n))