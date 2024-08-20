entry = input().split()
entry = [eval(i) for i in entry]

time = 24
if entry[0] < entry[1]:
    time = entry[1] - entry[0]
if entry[0] > entry[1]:
    time = time - entry[0] + entry[1]
print(f"O JOGO DUROU {time} HORA(S)")