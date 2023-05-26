s=input()
length=len(str(s))
sum=0
for i in range(length):
    a=s[i]
    if a.isdigit():
        sum+=int(a)
print(sum)