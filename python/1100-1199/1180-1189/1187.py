op = str.upper(input())
entry = [[float(input()) for j in range(12)]for i in range(12)]
values1, values2 = 1, 11

for i in range(12):
    del entry[i][values2:12]
    del entry[i][0:values1]    
    values2 -= 1
    values1 += 1
entry = list(map(lambda x: sum(x), entry))
entry = sum(entry)
if op == "M":
    entry /= 30
print(f"{entry:.1f}")