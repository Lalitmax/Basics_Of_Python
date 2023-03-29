
def fact(n):
    if n==1:
     return 1
    else:
        return n*fact(n-1)

def sum(a,b):
    return a+b

def multi(a,b):
    return a*b

def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:

        return fibo(n-1)+fibo(n-2)

def count(n):
    if n//10==0:
        return 1
    else:
        return 1+count(n//10)

 