from math import sqrt

def prime(x):
    if x == 2: return True
    if x < 2 or x%2 == 0: return False
    return not any(x % i == 0 for i in range (3, int(sqrt(x)) + 1, 2))

test_num = 2
prime_count = 1

while (prime_count < 10001):
    test_num = test_num + 1
    if (prime(test_num)):
        prime_count += 1

print(test_num)
