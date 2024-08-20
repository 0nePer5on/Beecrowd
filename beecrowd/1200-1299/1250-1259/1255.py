num = int(input())
for n in range(num):
    entry = input().lower().replace(" ", '')
    values = {}
    for i in entry:
        if not i in values.keys():
            values[i] = 1
        else:
            values[i] += 1
    values = dict(sorted(values.items(), key=lambda x: x[1], reverse=True))
    bigger = 0
    txt = ""
    for i in values.keys():
        if values[i] >= bigger:
            bigger = values[i]
            txt += i
        else:
            break
    txt = sorted(txt)
    print("".join(txt))