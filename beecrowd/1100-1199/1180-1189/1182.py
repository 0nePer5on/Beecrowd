column = int(input())
op = str.upper(input())
value = [[float(input()) for j in range(12)] for i in range(12)]
total = 0
for i in range(12):
    total += value[i][column]
if op == 'M':
    total /= 12
print(f"{total:.1f}")