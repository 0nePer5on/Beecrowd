media = 0
while True:
    entry = float(input())
    if entry >= 0 and entry <= 10:
        if media != 0:
            print(f"media = {(media + entry) / 2:.2f}")
            stop = False
            while True:
                print("novo calculo (1-sim 2-nao)")
                value = int(input())
                if value == 1:
                    break
                if value == 2:
                    stop = True
                    break
            if stop:
                break
            media = 0
        else:
            media = entry
    else:
        print("nota invalida")