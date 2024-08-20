entry = float(input())
total = 0

if entry > 2000 and entry <= 3000:
    total = (entry - 2000) * 0.08
if entry > 3000 and entry <= 4500:
    total = 1000 * 0.08 + (entry - 3000) * 0.18
if entry > 4500:
    total = 1000 * 0.08 + 1500 * 0.18 + (entry - 4500) * 0.28
if entry <= 2000:
    print("Isento")
else:
    print(f"R$ {total:.2f}")