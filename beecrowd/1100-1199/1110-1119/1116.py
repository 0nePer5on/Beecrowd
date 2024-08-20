num = int(input())
for i in range(num):
    entry = list(map(int, input().split()))
    if entry[1] == 0:
        print("divisao impossivel")
    else:
        print(round(entry[0] / entry[1], 1))