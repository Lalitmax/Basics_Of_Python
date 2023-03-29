key=int(input())
isfound=False
li=[1,4,2,3,6,77,12]

for i in range(len(li)):
	if key==li[i]:
		print(i)
		isfound=True
		break
if isfound is False:
	print(-1)
