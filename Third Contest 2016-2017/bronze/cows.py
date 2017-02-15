def change(b):
    asdf = b.split(' ')
    return int(asdf[0]), int(asdf[1])

thing = open("crossroad.in", 'r')
num = int(thing.readline())
ids = []
side = []
count = 0
for x in range(num):
    b,c = change(thing.readline())
    if b not in ids:
        ids.append(b)
        side.append(c)
    elif b in ids:
        if side[ids.index(b)] != c:
            count += 1
            side[ids.index(b)] = c
print (count)
answer = open("crossroad.out", 'w')
answer.write(str(count))
answer.close()
