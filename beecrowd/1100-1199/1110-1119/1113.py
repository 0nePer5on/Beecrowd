while True:
    entry = list(map(int, input().split()))
    if entry[0] == entry[1]:
        break
    if entry[0] < entry[1]:
        print("Crescente")
    else:
        print("Decrescente")