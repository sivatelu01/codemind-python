a=int(input())
c=str(a)
if a<0:
    if c[-1]!="0":
        b=c[:0:-1]
        print("-"+b)
    else:
        b=c[-2:0:-1]
        print("-"+b)
elif c[-1]=="0":
    b=c[-2::-1]
    print(b)
else:
    print(c[::-1])