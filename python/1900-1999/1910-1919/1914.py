num = int(input())
for i in range(num):
    entry1 = input().split()
    entry2 = list(map(int, input().split()))
    values = {}
    result = 0
    if entry1[1] == "PAR":
        values = {0:entry1[0], 1:entry1[2]}
    else:
        values = {0:entry1[2], 1:entry1[0]}
    if sum(entry2) % 2 == 1:
        result = 1
    print(values[result])