
def bubbleSort(arr, n) :
    #Your code goes here
    for i in range(n - 1):
        flag = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                
                # Swap adjacent elements.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True

        # If array already sorted, break.
        if flag is False:
            break

    return

arr=[5,2,3,77,33,1,2,0]
n=len(arr)
bubbleSort(arr, n)
print(arr)
