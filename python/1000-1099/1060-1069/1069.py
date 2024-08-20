nEntry = int(input())
for entry in range(nEntry):
    total, menor = 0, 0
    value = input()
    for i in value:
        if i == '<':
            menor += 1
        if i == ">" and menor > 0:
            menor -= 1
            total += 1
    print(total)
