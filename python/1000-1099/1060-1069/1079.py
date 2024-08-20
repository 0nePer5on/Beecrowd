num = int(input())
for i in range(num):
    entry = list(map(float, input().split()))
    print(f"{(entry[0] * 2 + entry[1] * 3 + entry[2] * 5) / 10:.1f}")