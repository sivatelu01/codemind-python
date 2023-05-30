n=int(input())
l=len(str(n))
b=str(n)
sum=0
for i in range(1,l+1):
    a=(int(b[i-1]))**i
    sum+=a
if n==sum:
    print(True)
else:
    print(False)