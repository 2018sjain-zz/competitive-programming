def isPal(n):
    val = str(n)
    for i in range (int(len(val)/2)):
        if val[i] != val[len(val) - 1 - i]:
            return False
    return True

top = 101
for x in range (100,1000):
    for y in range (x,1000):
        val = x * y
        if isPal(val) and val > top:
            top = val
print(top)
