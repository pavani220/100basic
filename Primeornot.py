n=3
if n<2:
    print("no")
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("no")
        break
else:
    print("yes")
