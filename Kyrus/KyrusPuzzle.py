def getFactor(n):
    # Euler#5
    # Returns a factor of the integer 'n'
    # Returns None if n is prime
    if n == 2 or n == 3:
        return None

    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3

    # Using 6k +- 1 optimization
    # https://en.wikipedia.org/wiki/Primality_test
    i = 5
    # Only need to check for factors <= sqrt(n)
    # This can also be expressed as: factor^2 <= n
    while i * i <= n:
        if n % i == 0:  # this is checking the 6k - 1 factor
            return i
        elif n % (i + 2) == 0:  # this is checking the 6k + 1 factor
            return (i+2)
        i += 6
    return None


def primeFactors(n):
    # map of "primeFactor" to "power"
    # e.g. 2^3, 3^4, 5^2, etc.
    factorMap = {}
    temp = n
    while temp != 1:
        factor = getFactor(temp)
        # factors.get(): Check if key exists. If not, set default value of 1
        # https://stackoverflow.com/a/1602964
        if factor is None:
            factorMap[temp] = factorMap.get(temp, 0) + 1
            break
        factorMap[factor] = factorMap.get(factor, 0) + 1
        temp = temp // factor
    return factorMap


# main
if __name__ == "__main__":
    # equation1: a^2 * b * c^2 * g = 5100
    n = 5100
    factors1 = primeFactors(n)
    print(f"Prime factorization of {n}: {factors1}")

    # equation 2: a * b^2 * e * f^2 = 33462
    n = 33462
    factors2 = primeFactors(n)
    print(f"Prime factorization of {n}: {factors2}")
    # since 'a' and 'b' are in both eq1 and eq2, we can narrow down these two specifically
    # find potential 'a' and 'b' values
    a, b = [], []
    for key2, power2 in factors2.items():
        for key1, power1 in factors1.items():
            if power1 % 2 == 0 and key2 == key1:
                # a is a^2 in equation 1; a is just 'a' in eq2
                a.append(key1)
            if power2 % 2 == 0 and key2 == key1:
                b.append(key1)

    print(f"Potential 'a' values: {a}")
    print(f"Potential 'b' values: {b}")

    # equation 3: a * c^2 * d^3 = 17150
    n = 17150
    factors3 = primeFactors(n)
    print(f"Prime factorization of {n}: {factors3}")

    # equation 4: a^3 * b^3 * c * d * e^2 = 914760
    n = 914760
    factors4 = primeFactors(n)
    print(f"Prime factorization of {n}: {factors4}")

    a, b, c, d, e = 0, 0, 0, 0, 0
    # iterate through factors 4 to verify a, b, c, d, e values
    for key, power in factors4.items():
        # check for a or b values
        if power == 3:
            if key in factors3 and factors3[key] == 1 and factors2[key] == 1 and factors1[key] == 2:
                a = key
            elif key in factors2 and factors2[key] == 2 and factors1[key] == 1:
                b = key
        # check for c or d
        elif power == 1:
            if factors3[key] == 2 and factors1[key] == 2:
                c = key
            elif factors3[key] == 3:
                d = key
        # check for e
        elif power == 2 and factors2[key] == 1:
            e = key
    # g is the last factor in factors1 not picked
    g = [x for x in factors1.keys() if x not in [a, b, c]].pop()
    # f is the last factor in factors2 not picked
    f = [x for x in factors2.keys() if x not in [a, b, e]].pop()
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}, g: {g}")

    # Verify
    print(f"Equation1: {a**2 * b * c**2 * g}")
    print(f"Equation2: {a * b**2 * e * f**2}")
    print(f"Equation3: {a * c**2 * d**3}")
    print(f"Equation4: {a**3 * b**3 * c * d * e**2}")
