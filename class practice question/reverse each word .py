
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	string=string.split()
	new_str=""
	for i in string:
		str=i[ : : -1]
		new_str+=str+" "

	return new_str


#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)