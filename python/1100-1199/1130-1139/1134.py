alcool = gas = diesel = 0

while True:
    entry = int(input())
    if entry == 1:
        alcool += 1
    if entry == 2:
        gas += 1
    if entry == 3:
        diesel += 1
    if entry == 4:
        break
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gas}")
print(f"Diesel: {diesel}")