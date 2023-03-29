# find duplicate

def find_duplicat(arr,n):
	for i in range(n):
		j=0
		while(j<n):
			if i!=j:
				if arr[i]==arr[j]:
					return arr[i]
					break
			j=j+1


arr=[1,2,3,4,5,6,7,34,5]
n=len(arr)
find_value=find_duplicat(arr,n)
print(find_value)
