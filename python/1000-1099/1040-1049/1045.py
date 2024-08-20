entry = input().split()
entry = [eval(i) for i in entry]
entry.sort(reverse=True)

if entry[0] >= entry[1] + entry[2]:
    print("NAO FORMA TRIANGULO")
else:
    if entry[0]**2 == entry[1]**2 + entry[2]**2:
        print("TRIANGULO RETANGULO")
    if entry[0]**2 > entry[1]**2 + entry[2]**2:
        print("TRIANGULO OBTUSANGULO")
    if entry[0]**2 < entry[1]**2 + entry[2]**2:
        print("TRIANGULO ACUTANGULO")
    if entry[0] == entry[1] and entry[0] == entry[2]:
        print("TRIANGULO EQUILATERO")
    if (entry[0] == entry[1] and entry[0] != entry[2]) or (entry[1] == entry[2] and entry[0] != entry[1]) or (entry[0] == entry[2] and entry[0] != entry[1]):
        print("TRIANGULO ISOSCELES")