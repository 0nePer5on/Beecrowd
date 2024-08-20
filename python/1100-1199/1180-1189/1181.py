line = int(input())
op = str.upper(input())
value = [[float(input()) for j in range(12)] for i in range(12)]
total = sum(value[line])
if op == 'M':
    total /= len(value[line])
print(f"{total:.1f}")