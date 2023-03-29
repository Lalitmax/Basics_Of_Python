def count_digit(n):
    if n//10==0:
        return 1
    else:
        return 1+count_digit(n//10)

n=int(input("Enter digits : "))
print("count  = ",count_digit(n))