numbers = list()
for i in range(4):
    numbers.append(int(input()))

total = numbers[0] * numbers[1] - numbers[2] * numbers[3]
print(f"DIFERENCA = {total}")