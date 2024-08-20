s, i = 0, 0
num, den = 1, 1
while True:
    s += num / den
    i += 1
    num += 2
    den = 2**i
    if num == 39:
        break
print(f"{s:.2f}")