import math

num = int(input())
for i in range(num):
    entry = list(map(int, input().split()))
    value = math.gcd(entry[0], entry[1])
    print(value)