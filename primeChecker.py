primes=[]
iIsPrime=True
for i in range(3,1000):
    for p in primes:
        if round(i/p) == i/p:
            iIsPrime=False
            break
    if iIsPrime == True:
        primes.append(i)
    iIsPrime=True
print(primes)

