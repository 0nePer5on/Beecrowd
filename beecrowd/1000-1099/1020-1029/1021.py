entry = input()
money = [100, 50, 20, 10, 5, 2]
coins = [100, 50, 25, 10, 5, 1]
values = entry.split('.')
values = [eval(i) for i in values]
print("NOTAS:")
for i in money:
    print(f"{int(values[0] / i)} nota(s) de R$ {i:.2f}")
    values[0] %= i
if values[0] == 1:
    values[1] += 100
print("MOEDAS:")
for i in coins:
    print(f"{int(values[1] / i)} moeda(s) de R$ {i / 100:.2f}")
    values[1] %= i