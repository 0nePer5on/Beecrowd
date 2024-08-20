media = 0
pos = 0
for i in range(6):
    entry = float(input())
    if entry > 0:
        pos += 1
        media += entry
print(f"{pos} valores positivos")
print(f"{media / pos:.1f}")