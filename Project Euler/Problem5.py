def gcd(x,y):
    while y != 0:
        (x , y) = (y, x%y)
    return x

def lcm(x,y):
    return (x*y)//gcd(x,y)

vals = [i for i in range(1,21)]
for x in range (len(vals)-1):
    vals[x+1] = lcm(vals[x],vals[x+1])
    
print (vals[19])
