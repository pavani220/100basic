a="123"
n=int(a)
res=""
while n>0:
    d=n%10
    res=res+str(d)
    n=n//10

print(res)