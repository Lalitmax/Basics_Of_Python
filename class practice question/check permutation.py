
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    cnt=0
    for i in string1:
        if i in string2:
             cnt+=1

    if cnt==len(string1):
         return True
    else:
         return False
        

























	


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

