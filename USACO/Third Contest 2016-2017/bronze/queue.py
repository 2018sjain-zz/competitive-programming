def change(b):
    asdf = b.split(' ')
    return (int(asdf[0]), int(asdf[1]))

thing = open("cowqueue.in", 'r')

num = int(thing.readline())
stuff = []
for x in range (num):
    stuff.append(change(thing.readline()))

stuff.sort(key = lambda tup: tup[0])
time = 0

for a,q in stuff:
    if a > time:
        time = time + (a - time) + q
    else:
        time = time + q

answer = open("cowqueue.out", 'w')
answer.write(str(time))
answer.close()
