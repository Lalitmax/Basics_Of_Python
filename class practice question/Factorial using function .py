
def factoral(n):

    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


print("factorial = ",factoral(5))

print("factorial = ",factoral(3))

print("factorial = ",factoral(2))