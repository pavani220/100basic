'''n="mom"
d=len(n)
res=""
i=d-1
while i>=0:
    res=res+n[i]
    i-=1
print(res)
if n==res:
    print("palindrome")

'''
a="121"
u=int(a)
temp=a
rev=""
while u>0:
    d=u%10
    rev=rev +str(d)
    u=u//10
print(rev)
if rev==temp:
    print("yes")
else:
    print("no")