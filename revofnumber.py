n=123
res=" "
while n>0:
    d=n%10
    res=res+str(d)
    n=n//10
print(res)