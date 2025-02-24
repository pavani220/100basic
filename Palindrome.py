n="mom"
d=len(n)
res=""
i=d-1
while i>=0:
    res=res+n[i]
    i-=1
print(res)
if n==res:
    print("palindrome")
    
    