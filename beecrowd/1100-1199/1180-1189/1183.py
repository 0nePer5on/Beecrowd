op = str.upper(input())
entry = [[float(input()) for j in range(12)]for i in range(12)]
values = 1

for i in range(12):
    del entry[i][0:values]
    values += 1
entry = list(map(lambda x: sum(x), entry))
entry = sum(entry)
if op == "M":
    entry /= 66
print(f"{entry:.1f}")