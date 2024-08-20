import math

num = int(input())
for i in range(num):
    value1 = int(input(), 2)
    value2 = int(input(), 2)
    if math.gcd(value1, value2) > 1:
        print(f"Pair #{i + 1}: All you need is love!")
    else:
        print(f"Pair #{i + 1}: Love is not all you need!")