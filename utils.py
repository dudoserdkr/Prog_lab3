def factorial(a):
    if a == 1 or a == 0:
        return 1
    
    return a*(a-1)


def nsd(a,b):
    while b > 0:
        a, b = b, a % b
    return a


def nsk(n):
    a = 1
    for x in range(2, n+1):
        a = a * x // nsd(a, x)
    return a