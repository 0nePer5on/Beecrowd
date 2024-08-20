info = {'C':0, 'R':0, 'S':0}
num = int(input())
for i in range(num):
    entry = input().split()
    info[entry[1]] += int(entry[0])
total = sum(info.values())
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {info.get('C')}")
print(f"Total de ratos: {info.get('R')}")
print(f"Total de sapos: {info.get('S')}")
print(f"Percentual de coelhos: {info.get('C') * 100 / total:.2f} %")
print(f"Percentual de ratos: {info.get('R') * 100 / total:.2f} %")
print(f"Percentual de sapos: {info.get('S') * 100 / total:.2f} %")