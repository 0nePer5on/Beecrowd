odd, even = [], []
for n in range(15):
    entry = int(input())
    if entry % 2 == 0:
        even.append(entry)
    else:
        odd.append(entry)
    if len(even) == 5:
        for i in range(len(even)):
            print(f"par[{i}] = {even[i]}")
        even.clear()
    if len(odd) == 5:
        for i in range(len(odd)):
            print(f"impar[{i}] = {odd[i]}")
        odd.clear()
for i in range(len(odd)):
    print(f"impar[{i}] = {odd[i]}")
for i in range(len(even)):
    print(f"par[{i}] = {even[i]}")