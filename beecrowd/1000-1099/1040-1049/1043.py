entry = input().split()
entry = [eval(i) for i in entry]
if entry[0] + entry[1] > entry[2] and entry[0] + entry[2] > entry[1] and entry[1] + entry[2] > entry[0]:
    print(f"Perimetro = {sum(entry):.1f}")
else:
    print(f"Area = {((entry[0] + entry[1]) * entry[2]) / 2:.1f}")