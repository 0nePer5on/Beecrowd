i, j = 1, 7
while i <= 9:
    for n in range(3):
        print(f"I={i} J={j - n}")
    j += 2
    i += 2