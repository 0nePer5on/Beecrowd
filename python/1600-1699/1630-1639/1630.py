import math

while True:
    try:
        entry = list(map(int, input().split()))
        num = (entry[0] * 2 + entry[1] * 2) / math.gcd(entry[0], entry[1])
        print(int(num))
    except EOFError:
        break