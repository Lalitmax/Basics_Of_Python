
def lar_col_sum(lst):
    m=len(lst[0])
    n=len(lst)
    max_sum=-123345678
    max_index=-1
    for i in range(m):
        sum=0
        for j in lst:
            sum +=j[i]
        if sum>max_sum:
            max_sum=sum
            max_index=i
    return max_sum,max_index


lst=[[1,4,2,3],[6,23,4,5],[9,2,1,1]]
larg_sum=lar_col_sum(lst)
# print largest number 
print(larg_sum)
