n=int(input())
a=""
for i in range(n,0,-1):
    a=chr(65+i-1)+" "
    print(a*i) 