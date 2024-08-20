num = int(input())
for n in range(num):
    total = 0
    nValues = int(input())
    for i in range(nValues):
        entry = input()
        for j in range(len(entry)):
            total += ord(entry[j]) - 65 + i + j
    print(total)