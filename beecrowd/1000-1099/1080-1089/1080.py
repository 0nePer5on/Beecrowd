num = 0
pos = 0
for i in range(100):
    entry = int(input())
    if entry > num:
        num = entry
        pos = i + 1
print(num)
print(pos)