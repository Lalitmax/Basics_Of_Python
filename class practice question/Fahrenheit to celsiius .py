
# fahrenheit to celsius

def fehtocel(s,e,w):
    while(s<=e):
        c=(s-32)/(9/5)
        print(s, " ",int(c))
        s=s+w

s=int(input())
e=int(input())
w=int(input())
fehtocel(s,e,w)