n=int(input())
a=0
for i in range(1,n+1):
    if i==1 or i==n or i==2:
        print("*"*i)
    else:
        a=a+1
        print("*"+" "*(a)+"*")