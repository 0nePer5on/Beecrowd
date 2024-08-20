num = int(input())
for n in range(num):
    entry = int(input())
    value, i = 0, 1
    while True:
        if value > entry or entry == 1:
            print(f"{entry} nao eh perfeito")
            break
        if value == entry:
            print(f"{entry} eh perfeito")
            break
        value += i
        i += 1