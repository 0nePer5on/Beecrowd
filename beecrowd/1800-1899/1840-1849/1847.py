entry = list(map(int, input().split()))
mood = True
if entry[0] == entry[1]:
    if entry[0] >= entry[2]:
        mood = False
if entry[0] > entry[1]:
    if entry[1] >= entry[2]:
        if entry[0] - entry[1] <= entry[1] - entry[2]:
            mood = False

if entry[0] < entry[1]:
    if entry[1] > entry[2]:
        mood = False
    else:
        if entry[0] - entry[1] < entry[1] - entry[2]:
            mood = False
if mood:
    print(":)")
else:
    print(":(")