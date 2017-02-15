def change(b):
    asdf = b.split(' ')
    return int(asdf[0]), int(asdf[1])

thing = open("helpcross.in", 'r')

numCh, numCo = change(thing.readline())
timesCh = [int(thing.readline()) for i in range(numCh)]
timesCo = [change(thing.readline()) for i in range(numCo)]

timesCo.sort(key = lambda tup: len(list(filter(lambda x: ((x >= tup[0]) and (x <= tup[1])),timesCh))))

count = 0

for a,b in timesCo:
    for x in range (len(timesCh)):
        if timesCh[x] >= a and timesCh[x] <= b:
            count += 1
            timesCh.pop(x)
            break

print(count)

answer = open("helpcross.out", 'w')
answer.write(str(count))
answer.close()
