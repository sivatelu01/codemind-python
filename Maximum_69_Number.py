n=input()
res=""
for i in range(len(n)):
    k=n[i]
    if k=="6":
        res+="9"
        break
    else:
        res+=k
print(res+n[i+1:])