entry = list(map(int, input().split()))
total = 0
for i in range(entry[len(entry) - 1]):
    total += i + entry[0]
print(total)