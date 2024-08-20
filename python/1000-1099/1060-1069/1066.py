odd, even, pos, neg = 0, 0, 0, 0
for i in range(5):
    entry = int(input())
    if entry % 2 == 0:
        even += 1
    else:
        odd += 1
    if entry > 0:
        pos += 1
    if entry < 0:
        neg += 1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")