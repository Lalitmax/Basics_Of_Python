x=input("Enter the number ")

h=True

for i in range(len(x)):
    if x[i]!=x[~i]:
        h=False
        break

if h:
    print("Transaction may proceed ")
else:
    print("Transaction declined")