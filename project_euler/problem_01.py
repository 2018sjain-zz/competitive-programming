val = 0
for number in range(1000):
    if not number % 3 or not number % 5:
        val += number
print (val)
