thing = open("pairup.in", 'r')
num = int(thing.readline())

tot = 0
pop = []
for x in range(num):
    vals = thing.readline()
    if vals == '':
        break
    stuff = vals.split(' ')
    for y in range(int(stuff[0])):
        pop.append(int(stuff[1]))
        
pop.sort()
top = 0
while (len(pop) > 1):
    temp = pop[0] + pop[len(pop)-1]
    if temp > top:
        top = temp
    del pop[len(pop)-1]
    del pop[0]

if len(pop) == 1:
    if pop[0] > top:
        top = pop[0]

count = int(top)

answer = open("pairup.out", 'w')
answer.write(str(count))
answer.close()
