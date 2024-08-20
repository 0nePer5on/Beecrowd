for i in range(3):
    count = 0
    while True:
        entry = input()
        if entry == "caw caw":
            break
        n = 2
        for j in entry:
            if j == "*":
                count += 2 ** n
            n -= 1
    print(count)