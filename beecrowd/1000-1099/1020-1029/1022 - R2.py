def MultDiv(values, operator):
    if operator == 2:
        num = values[0] * values[2]
        den = values[1] * values[3]
    else:
        num = int(values[0] * values[3])
        den = int(values[1] * values[2])

    find = False
    for i in range(1, abs(num)):
        for j in range(1, den):
            if i * den == j * abs(num):
                if num < 0:
                    i *= -1
                print(f"{num}/{den} = {i}/{j}")
                find = True
                break
        if find:
            break
    if not find:
        print(f"{num}/{den} = {num}/{den}")

def SumSub(values, operator):
    n1 = values[0] * values[3]
    n2 = values[1] * values[2]
    d = values[1] * values[3]
    if operator == 0:
        total = n1 + n2
    else:
        total = n1 - n2

    find = False
    for i in range(1, abs(total)):
        for j in range(1, d):
            if i * d == j * abs(total):
                if total < 0:
                    i *= -1
                print(f"{total}/{d} = {i}/{j}")
                find = True
                break
        if find:
            break
    if not find:
        print(f"{total}/{d} = {total}/{d}")


num = int(input())
operators = ['+', '-', '*', '/']
op = -1
for n in range(num):
    entry = list(input().split())
    for i in range(len(operators)):
        if operators[i] in entry:
            op = i
            break
    aux = entry
    for i in entry:
        if i in operators:
            aux.remove(i)
    aux = [eval(i) for i in aux]
    if op == 0 or op == 1:
        SumSub(aux, op)
    else:
        MultDiv(aux, op)