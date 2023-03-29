def checkMember(n):
#Implement Your Code Here
    if (n == 0 or n == 1):
        return True

    a = 0
    b = 1

    while (True):

        add = a + b

        if (add == n):
            return True
        elif (add > n):
            break

        b = a
        a = add
    return False
      
    

n=int(input())

if(checkMember(n)):
    print("true")
else:
    print("false")