s=input()
length_string=len(s)
large=ord(s[0])
for i in range(1,length_string):
    a=ord(s[i])
    if large<a:
        large=a
print(chr(large))
    