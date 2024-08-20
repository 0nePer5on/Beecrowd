n1, n2 = int(input()), 0
while True:
    n2 = int(input())
    if n2 > n1:
        break
count = 1
total = n1
while True:
    n1 += 1
    total += n1
    count += 1
    if total > n2:
        break
print(count)