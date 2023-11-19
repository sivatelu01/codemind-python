m,n=map(int,input().split())
mat=[]
for s in range(m):
    arr=list(map(int,input().split()))
    mat.append(arr)
sum=0   
for i in range(m):
    for j in range(n):
        if i==j or i+j==n-1:
            k=mat[i][j]
            sum+=k
print(sum)