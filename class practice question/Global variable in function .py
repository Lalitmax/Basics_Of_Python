total = 45  # Global variable
def sum(a,b):
    total=a+b
    # if i want to change globally then do 
    ''' 
    global total 
     total= a+b
    '''
    print("inside function =",total)
    
sum(4, 7)
print("outside function =",total)