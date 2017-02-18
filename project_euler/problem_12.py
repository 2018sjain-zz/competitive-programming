def divs(n):
    count = 0
    for x in range(1, int(n/2) + 1):
        if n % x == 0: count += 1
    return count

curr = 1
while True == True:
    num = (curr*(curr + 1))/2
    if divs(num) > 500:
        print(num)
        break
    curr += 1
