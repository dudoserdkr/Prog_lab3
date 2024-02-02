def factorial(a):
    if a == 1 or a == 0:
        return 1
    
    return a*(a-1)


def nsd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
