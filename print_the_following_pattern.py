n=int(input())
left_spaces=0
right_spaces=(n-3)
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "+"  "*(n-2)+"* ")
    else:
        print("* "+("  "*left_spaces)+"* "+("  "*right_spaces)+"* ")
        left_spaces+=1
        right_spaces-=1