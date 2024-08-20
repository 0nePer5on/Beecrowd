intervals = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
entry = float(input())
if entry >= 0 and entry <= 25:
    print(f"Intervalo {intervals[0]}")
elif entry > 25 and entry <= 50:
    print(f"Intervalo {intervals[1]}")
elif entry > 50 and entry <= 75:
    print(f"Intervalo {intervals[2]}")
elif entry > 75 and entry <= 100:
    print(f"Intervalo {intervals[3]}")
else:
    print("Fora de intervalo")