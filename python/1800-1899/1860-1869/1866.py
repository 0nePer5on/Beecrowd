num = int(input())
for i in range(num):
    entry = int(input())
    S = 0
    for j in range(entry):
        S *= -1
        S += 1
    print(S)