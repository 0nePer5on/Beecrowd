def primo(n):
    while True:
        n += 1
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 2:
            break
    return n

def MultDiv(values, operator):
    if operator == 2:
        num = values[0] * values[2]
        den = values[1] * values[3]
    else:
        num = int(values[0] * values[3])
        den = int(values[1] * values[2])

    num2, den2 = num, den
    simpl = 2
    while True:
        if simpl > num2 and simpl > den2:
            break
        if num2 % simpl == 0 and den2 % simpl == 0:
            num2 = int(num2 / simpl)
            den2 = int(den2 / simpl)
        else:
            simpl = primo(simpl)

    print(f"{num}/{den} = {num2}/{den2}")

def SumSub(values, operator):
    n1 = values[0] * values[3]
    n2 = values[1] * values[2]
    d = values[1] * values[3]
    if operator == 0:
        total = n1 + n2
    else:
        total = n1 - n2

    totalS, d2 = total, d
    simpl = 2
    while True:
        if simpl > totalS and simpl > d2:
            break
        if totalS % simpl == 0 and d2 % simpl == 0:
            totalS = int(totalS / simpl)
            d2 = int(d2 / simpl)
        else:
            simpl = primo(simpl)

    print(f"{total}/{d} = {totalS}/{d2}")

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