val = 0
for i in range(5):
    entry = int(input())
    if entry % 2 == 0:
        val += 1
print(f"{val} valores pares")