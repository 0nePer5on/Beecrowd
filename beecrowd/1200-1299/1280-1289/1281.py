nEntry = int(input())
for entry in range(nEntry):
    nProducts = int(input())
    products = dict()
    for n in range(nProducts):
        product = input()
        value = product.split()
        buff = {value[0]:float(value[1])}
        products.update(buff)
    nPurchase = int(input())
    total = 0
    for n in range(nPurchase):
        product = input()
        value = product.split()
        total += products[value[0]] * int(value[1])
    print(f"R$ {total:.2f}")