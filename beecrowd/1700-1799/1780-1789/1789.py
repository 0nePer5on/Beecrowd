while True:
    try:
        num = input()
        entry = list(map(int, input().split()))
        if max(entry) < 10:
            print(1)
        elif max(entry) >= 20:
            print(3)
        else:
            print(2)
    except EOFError:
        break