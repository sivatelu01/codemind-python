n=int(input())
for i in range(n):
    a=input()
    f=0
    for j in a:
        if j.isdigit():
            f=1
            break
    if f==1:
        print("Yes")
    else:
        print("No")
    