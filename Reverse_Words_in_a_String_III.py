s=input()
a=""
res=""
for i in s:
    if i==" ":
        res+=a[::-1]+" "
        a=""
    else:
        a+=i
res+=a[::-1]
print(res)
    