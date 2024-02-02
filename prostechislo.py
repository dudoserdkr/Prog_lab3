
n = int(input())

def proste(el):
    for d in range(2, int(el**0.5)+1):
        if el % d == 0:
            return False
    return True
if proste(n) == True:
    print("Це число просте")
else:
    print("Це число не є просте")


