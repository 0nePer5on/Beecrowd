num = int(input())
for n in range(num):
    entry = int(input())
    if entry == 0:
        print("NULL")
    elif entry > 0:
        if entry % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else:
        if entry % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")