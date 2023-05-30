n=int(input())
a=n*n
b=str(n)
l=len(b)
c=""
g=""
for i in range(l,0,-1):
    c+=b[i-1]
d=int(c)
e=d*d
f=str(e)
k=len(f)
for j in range(k,0,-1):
    g+=f[j-1]
if int(g)==a:
    print(True)
else:
    print(False)