from math import sqrt

def prime(x):
    if x == 2: return True
    if x < 2 or x%2 == 0: return False
    return not any(x % i == 0 for i in range (3, int(sqrt(x)) + 1, 2))

tot = 0
for x in range (1, 2000001):
    if prime(x):
        tot += x

print(tot)
