entry = float(input())
salReaj = 0
reajust = 0

if entry <= 400:
    salReaj = entry * (15 / 100)
    reajust = 15
if entry > 400 and entry <= 800:
    salReaj = entry * (12 / 100)
    reajust = 12
if entry > 800 and entry <= 1200:
    salReaj = entry * (10 / 100)
    reajust = 10
if entry > 1200 and entry <= 2000:
    salReaj = entry * (7 / 100)
    reajust = 7
if entry > 2000:
    salReaj = entry * (4 / 100)
    reajust = 4
print(f"Novo salario: {entry + salReaj:.2f}")
print(f"Reajuste ganho: {salReaj:.2f}")
print(f"Em percentual: {reajust} %")