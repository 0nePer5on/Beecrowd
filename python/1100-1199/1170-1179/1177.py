entry = int(input())
num = 0
for i in range(1000):
    print(f"N[{i}] = {num}")
    num += 1
    if num == entry:
        num = 0