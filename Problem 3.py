def cheack(x):#cheack number on prime
    d = 2
    while d * d <= x and x % d != 0:
        d += 1
    return d * d > x
def fact(x): #search of factors
    result = []
    i = 2
    while i < x:
        if x % i == 0 and cheack(i):
            x /= i
            result.append(i)
        else:
            i += 1
    result.append(x)
    return result

print(int(max(fact(600851475143 ))))
