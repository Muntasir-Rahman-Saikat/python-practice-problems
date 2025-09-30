def isprime(m):
    import math
    for i in range(2,math.floor(m**.5)+1):
        print(i)
        if m%i!=0:
            pass
        else:
            return "Not a prime number"
    return "prime number"
print(isprime(25))

print(isprime(100))

