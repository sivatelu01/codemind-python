n=int(input())
a=n*n#81
c=str(a)#"81"
l=len(c)#2
b=""
sum=0
for i in range(l):
    d=c[i]
    sum+=int(d)
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")