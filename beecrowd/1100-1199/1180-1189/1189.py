op = str.upper(input())
entry = [[float(input()) for j in range(12)]for i in range(12)]
values = 0

entry.reverse()
for i in range(12):
    del entry[i][values:12]
    values += 1
entry.reverse()
values = 0
for i in range(12):
    del entry[i][values:12]
    values += 1
entry = list(map(lambda x: sum(x), entry))
entry = sum(entry)
if op == "M":
    entry /= 30
print(f"{entry:.1f}")