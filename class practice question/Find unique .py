# find unique

def find_uniwue(arr,n):
	for i in range(n):
		j=0
		while(j<n):
			if j!=i:
				if arr[i]==arr[j]:
                    
					break
			j=j+1
		if j==n:
			return arr[i]
            
	    

arr=[1,2,3,5,4,3,5]
n=len(arr)
find_value=find_uniwue(arr,n)
print(find_value)
