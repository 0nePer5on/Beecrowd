age = count = 0
while True:
    entry = int(input())
    if entry < 0:
        break
    count += 1
    age += entry
print(f"{age/count:.2f}")