n1, n2 = input().split()
n1, n2 = float(n1), float(n2)

if n1 == 0 and n2 == 0:
    print("Origem")
elif n1 == 0:
    print("Eixo Y")
elif n2 == 0:
    print("Eixo X")
else:
    if n1 > 0 and n2 > 0:
        print("Q1")
    if n1 < 0 and n2 > 0:
        print("Q2")
    if n1 < 0 and n2 < 0:
        print("Q3")
    if n1 > 0 and n2 < 0:
        print("Q4")