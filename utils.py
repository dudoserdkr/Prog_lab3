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


print(func1(625))
