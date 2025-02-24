start=0
end=10
primes=[]
even_primes=[]
for num in range(start,end+1):
    if num<2:
        continue
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        primes.append(num)
print(primes)
for j in primes:
    if j%2==0:
        even_primes.append(j)
print(even_primes)
    