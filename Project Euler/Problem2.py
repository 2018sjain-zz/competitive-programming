val = 0
PHI = 1.618033989398874989484820
power = 1
curr = round((PHI**power)/(5**(.5)), 0)
while curr < 4000000:
    if curr % 2 == 0:
        val += curr
    power += 1
    curr = round((PHI**power)/(5**(.5)), 0)
print(val)
