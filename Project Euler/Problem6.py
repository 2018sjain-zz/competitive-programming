val1 = 0
val2 = 0
for x in range (1, 101):
    val1 += (x**2)
    val2 += x
val2 = (val2**2)
print(val2-val1)
