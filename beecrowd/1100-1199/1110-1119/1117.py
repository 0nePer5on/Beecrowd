media = 0
while True:
    entry = float(input())
    if entry >= 0 and entry <= 10:
        if media != 0:
            print(f"media = {(media + entry) / 2}")
            break
        media = entry
    else:
        print("nota invalida")