#  find second largest number in a list 
# find largest number 


def findlargestnum(list):
    bigg_num=list[0]

    for i in list:
        if bigg_num<i:
            bigg_num=i
    
    return bigg_num



size=int(input("Enter size of list : "))
list=[]

for i in range(size):
    v=int(input())
    list.append(v)

lar_num=findlargestnum(list)
print(lar_num)