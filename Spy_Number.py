a=int(input())
b=str(a)
sum=0
product=1
for i in b:
    sum+=int(i)
    product*=int(i)
if sum==product:
    print("Spy Number")
else:
    print("Not Spy Number")