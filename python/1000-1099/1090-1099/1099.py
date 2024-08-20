num = int(input())
for n in range(num):
    odd = 0
    entry = list(map(int, input().split()))
    entry.sort()
    for i in range(entry[0], entry[1]):
        if i % 2 == 1 and not i == entry[0]:
            odd += i
    print(odd)