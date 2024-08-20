numbers = []
for i in range(20):
    entry = int(input())
    numbers.append(entry)
numbers.reverse()
for i in range(20):
    print(f"N[{i}] = {numbers[i]}")