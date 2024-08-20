entry = list(input().split())
entry = [eval(i) for i in entry]

MaiorAB1 = (entry[0] + entry[1] + abs(entry[0] - entry[1])) / 2
MaiorAB2 = (MaiorAB1 + entry[2] + abs(MaiorAB1 - entry[2])) / 2
print(f"{int(MaiorAB2)} eh o maior")