thing = open("circlecross.in", 'r')

data = thing.readline()
fixed = data

for x in range (len(data)):
    if x == len(data)-1:
        if data[x] == data[0]:
            fixed = fixed.replace(data[x], "")
    elif data[x] == data[x + 1]:
        fixed = fixed.replace(data[x], "")

ids = []
vals = []
for x in range (len(fixed)):
    if fixed[x] not in ids:
        ids.append(fixed[x])
    if len(ids) == int(len(fixed)/2):
        break

for x in ids:
    vals.append([pos for pos, char in enumerate(fixed) if char == x])

count = 0
for x in range(len(ids)-1):
    for y in range (x + 1, len(ids)):
        a,b = vals[x]
        c,d = vals[y]
        
        if c > a and d > b and b > c and a < d:
            count += 1

answer = open("circlecross.out", 'w')
answer.write(str(count))
answer.close()
