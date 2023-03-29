
def findlargest(li):
    n=len(li)
    m=len(li[0])
    isrow=0
    largest_sum=-2147483648
    index=0
    for i  in range(n):
        row_sum=0
        for j in range(m):
            row_sum+=li[i][j]
        if row_sum>largest_sum:
            largest_sum=row_sum
            index=i
    for i  in range(m):
        col_sum=0
        for j in range(n):
            col_sum+=li[j][i]
        if col_sum>largest_sum:
            largest_sum=col_sum
            index=i
            isrow+=1

    if isrow==0:
        print("row",index,largest_sum)
    else:
        print("column",index,largest_sum)



li=[[1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]]
findlargest(li)