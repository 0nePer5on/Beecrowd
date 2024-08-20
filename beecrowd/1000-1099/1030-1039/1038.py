products = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50 }
entry = input().split()
entry = [eval(i) for i in entry]
print(f"Total: R$ {products[entry[0]] * entry[1]:.2f}")