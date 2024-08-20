inter = gremio = draw = 0

while True:
    entry = list(map(int, input().split()))
    if entry[0] > entry[1]:
        inter += 1
    if entry[0] < entry[1]:
        gremio += 1
    if entry[0] == entry[1]:
        draw += 1
    print("Novo grenal (1-sim 2-nao)")
    choice = int(input())
    if choice == 2:
        break
print(f"{inter + gremio + draw} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{draw}")
if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")