start=0
end=10
primes=[]
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
'''start = 10
end = 50

primes = []
for num in range(start, end + 1):
    if num < 2:
        continue  # Skip numbers less than 2
    is_prime = True  # Assume the number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  # Found a divisor, so it's not prime
            break  # No need to check further
    if is_prime:
        primes.append(num)

print(f"Prime numbers between {start} and {end} are: {primes}")'''
