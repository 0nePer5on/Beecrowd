entry = input().split()
entry = [eval(i) for i in entry]

time = [0, 0]
total = (entry[2] * 60 + entry[3]) - (entry[0] * 60 + entry[1])
if total < 1:
    total += 24 * 60
time[0] = total // 60
time[1] = total % 60

print(f"O JOGO DUROU {time[0]} HORA(S) E {time[1]} MINUTO(S)\n");