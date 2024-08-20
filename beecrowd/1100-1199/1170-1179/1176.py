num = int(input())
for n in range(num):
    entry = int(input())
    n1, n2 = 0, 1
    for i in range(entry):
        aux = n2
        n2 += n1
        n1 = aux
    print(f"Fib({entry}) = {n1}")