m,n=map(int,input().split())
s=str(m)
a=len(s)
b=s[:n]
b=int(b)
c=s[a-n:]
c=int(c)
print(abs(b-c))