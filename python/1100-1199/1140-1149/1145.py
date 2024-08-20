entry = list(map(int, input().split()))
numbers = []
for i in range(1, entry[1] + 1):
    numbers.append(str(i))
    if i % entry[0] == 0:
        print(" ".join(numbers))
        numbers.clear()