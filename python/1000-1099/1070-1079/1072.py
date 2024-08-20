num = int(input())
inn, out = 0, 0
for n in range(num):
    entry = int(input())
    if entry >= 10 and entry <= 20:
        inn += 1
    else:
        out += 1

print(f"{inn} in\n{out} out")