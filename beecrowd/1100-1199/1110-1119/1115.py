while True:
    entry = list(map(int, input().split()))
    if entry[0] == 0 or entry[1] == 0:
        break
    if entry[0] > 0 and entry[1] > 0:
        print("primeiro")
    if entry[0] < 0 and entry[1] > 0:
        print("segundo")
    if entry[0] < 0 and entry[1] < 0:
        print("terceiro")
    if entry[0] > 0 and entry[1] < 0:
        print("quarto")