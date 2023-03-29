def recur_fibo(n):  
    if n ==0: 
        return 0
    elif n==1:
        return 1
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))



n=int(input())

print(recur_fibo(n-1))