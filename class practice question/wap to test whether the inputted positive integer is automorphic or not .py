d = "lalit max pandey yadav"
d = d.split()
new_list = []
new_list_2 = [d[i]+" " for i in range(2, len(d))]
strrequest = ""
for i in new_list_2:
    strrequest += i

print(strrequest)
