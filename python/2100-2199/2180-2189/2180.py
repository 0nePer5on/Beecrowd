import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

weight = int(input());
distance = 60000000
conf = 0
speed = 0

while conf != 10:
    if not is_prime(weight):
        weight += 1
    else:
        conf += 1
        speed += weight
        weight += 1
hours = math.floor(distance / speed)
print(f"{speed} km/h")
print(f"{hours} h / {math.floor(hours / 24)} d")