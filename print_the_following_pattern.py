n=int(input())
a="x"*n
for i in range(1,n+1):
    print(a[:i-1]+"0"+a[i:])