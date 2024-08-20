def defineM(num):
    return num
while True:
    entry = int(input())
    if entry == 0:
        break
    n1, n2 = 0, entry
    numbers = [[1] * entry] * entry
    numbers = [[defineM(numbers[i][j]) for j in range(entry)] for i in range(entry)]
    while True:
        n1 += 1
        n2 -= 1
        if n1 >= n2:
            break
        for i in range(n1, n2):
            for j in range(n1, n2):
                numbers[i][j] += 1
    # Resolucao de um random
    for i in range(len(numbers)):
        tx = ''
        for j in range(len(numbers)):
            tx += " %3d" %numbers[i][j]
        print(tx[1:])
    print("")

    # Minha resulucao
    # for i in range(len(numbers)):
    #     value = list(map(str, numbers[i]))
    #     txt = "  " + "   ".join(value)
    #     print(txt)
    # print("")