entry = int(input())
numbers = [100, 50, 20, 10, 5, 2, 1]

print(entry)
for i in numbers:
    print(f"{int(entry / i)} nota(s) de R$ {i},00")
    entry %= i