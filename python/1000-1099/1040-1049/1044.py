n1, n2 = input().split()
if int(n2) % int(n1) == 0 or int(n1) % int(n2) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")