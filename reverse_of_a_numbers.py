n=int(input())
l=len(str(n))
a=str(n)
b=""
for i in range(l,0,-1):
    b+=a[i-1]
print(b)
    