def factorize(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    factors = []
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            count += 1
            if n // i != i:
                factors.append(n // i)

    print(count)
    return factors
            
print(factorize(36))  