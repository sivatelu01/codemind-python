n=input()
temp=n
while(1):
    sum=0
    for i in temp:
        sum+=(int(i))
    if len(str(sum))==1:
        print(sum)
        break
    else:
        temp=str(sum)