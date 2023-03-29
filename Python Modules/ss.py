import re
string = "34/45j"
x = re.findall("\d+\/\d+", string)
sum = 0
for i in x:
    st = ''
    for j in i:

        if j >= '0' and j <= '9':
            st += j
        else:
            # print(st)
            sum += int(st)
            st = ''
print(sum)
