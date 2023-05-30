n=int(input())
a=len(str(n))
b=str(n)
large=int(b[0])
for i in range(1,a):
    c=int(b[i])
    if large<c:
        large=c
print(large)