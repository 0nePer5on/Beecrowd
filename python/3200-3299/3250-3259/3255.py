import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

order = {"O":0, "E":1, "I":2}
values = [0, 0, 0]
num = int(input())
for i in range(num):
    entry = list(input().split())
    start = order[entry[0]]
    val = int(entry[1])
    if not is_prime(val):
        continue