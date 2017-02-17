def change(b):
    asdf = b.split(' ')
    return (int(asdf[0]), int(asdf[1]), int(asdf[2]))

def around(num, broken, length):
    if len(broken) == 1:
        return length - 1
    val = broken.index(num)
    if val == 0:
        return (broken[1] - broken[0] - 1) + (broken[0] - 1)
    elif val == len(broken)-1:
        return (broken[val] - broken[val - 1] - 1) + (length - broken[val])
    else:
        return broken[val + 1] - broken[val - 1] - 2

def gottem(lights, line, length):
    for x in range (len(lights) - 1):
        if lights[x] - lights[x-1] - 1 >= line:
            return True
    if lights[0] - 1 >= line:
        return True
    elif length - lights[len(lights) - 1] + 1 >= line:
        return True
    return False

thing = open("maxcross.txt", 'r')

num, line, broken = change(thing.readline())
lights = [int(thing.readline()) for i in range(broken)]
lights.sort()
best = [around(i, lights, num) for i in lights]

count = 0
while True == True:
    if line == num:
        count = broken
        break
    if gottem(lights, line, num):
        break
    val = best.index(max(best))
    lights.pop(val)
    
    if val == 0:
        best[1] = around(lights[0], lights, num)
    elif val == len(best) - 1:
        best[val - 1] = around(val - 1, lights, num)
    else:
        best[val + 1] = around(lights[val], lights, num)
        best[val - 1] = around(lights[val -1], lights, num)
    count += 1
    best.pop(val)

print(count)

answer = open("maxcross.out", 'w')
answer.write(str(count))
answer.close()
