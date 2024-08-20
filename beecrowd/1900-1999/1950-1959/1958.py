def printValue(num):
    if entry == 0:
        if str(entry)[0] != '-':
            print(f"+{entry:.4E}")
            return
    if entry > 0:
        print(f"+{entry:.4E}")
        return
    print(f"{entry:.4E}")

entry = float(input())
printValue(entry)