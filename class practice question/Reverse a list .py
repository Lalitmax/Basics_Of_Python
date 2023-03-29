def reverse(li):
	length=len(li)
	for i in range(length//2):
        # li[i],li[-i-1] = li[-i-1],li[i]  # in jupyter not book
		temp=l[i]
		li[i]=li[-i -1]
		li[-i-1]=temp

l=[1,2,3,4,5,6,7,8,9]
reverse(l)	
print(l)