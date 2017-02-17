def prime(x):
    if x == 2:
        return True
    else:
        for number in range(3, x):
            if x % number == 0 or x%2 == 0:
                return False
        return True
lst = [2]
for i in range(3, 10001):
    if prime(i) == True:
        lst.append(i)
        if len
