i, j = 0, 1
while True:
    if i > 2:
        break
    for n in range(3):
        print(f"I={i} J={j + n}")
    i += 0.2
    j += 0.2
    i, j = round(i, 1), round(j, 1)
    if i == 1 or i == 2:
        i, j = round(i), round(j)