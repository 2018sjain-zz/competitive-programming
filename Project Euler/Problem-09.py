def pythag(a,b,c):
    return (a**2) + (b**2) == (c**2)

for x in range(1000):
    for y in range(x+1, 1000):
        for z in range (y+1, 1000):
            if x + y + z == 1000:
                if pythag(x,y,z):
                    print(x*y*z)
