

def  lenear_search(li,key):
	# li is the list and key is element to be search
	for i in range(len(li)):
		if key==li[i]:
			return i
	return -1

li=[5,2,3,177,44,23,5]
key=177
index=lenear_search(li,key)
print(index)