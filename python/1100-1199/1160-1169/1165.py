num = int(input())
for n in range(num):
    entry = int(input())
    count = 0
    for i in range(1, entry + 1):
        if entry % i == 0:
            count += 1
    if count == 2:
        print(f"{entry} eh primo")
    else:
        print(f"{entry} nao eh primo")