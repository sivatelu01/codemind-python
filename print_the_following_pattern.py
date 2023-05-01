n=int(input())
a=""
for i in range(1,n+1):
    a=a+str(chr(64+i))+" "
    print(a*n)
    a=