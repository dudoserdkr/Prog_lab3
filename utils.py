def factorial(a):
    if a == 1 or a == 0:
        return 1
    
    return a*(a-1)

def func1(a):
    while True:
        if a % 5 != 0 and a != 1 and a != 0:
            return False
        elif a == 1 or a == 0:
            break
        a //= 5

    return True

def proste(el):
    for d in range(2, int(el**0.5)+1):
        if el % d == 0:
            return "Це число не є просте"
    return "Це число є просте"

def nsd(a,b):
    while b > 0:
        a, b = b, a % b
    return a


def nsk(n):
    a = 1
    for x in range(2, n+1):
        a = a * x // nsd(a, x)
    return a