entry = list(map(int, input().split()))
value = 0
if entry[0] == entry[1]:
    value = entry[0]
else:
    value = max(entry)
print(value)