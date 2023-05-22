n=int(input())
a=0
for i in range(n):
    if (i==0):
        print("*")
    elif(i==n-1):
        print("*"*n)
    else:
        print("*"+" "*(a)+"*")
        a+=1