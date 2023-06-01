n=int(input())
a=abs(n)
l=len(str(a))
b=a**2
s=str(b)
if a==int(s[-l:]):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
