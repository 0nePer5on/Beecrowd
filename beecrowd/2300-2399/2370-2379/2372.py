INF = 99999

def cond(i, j, value):
    if i == j:
        return 0
    return value

num = list(map(int, input().split()))
G = [[INF] * num[0]] * num[0]
G = [[cond(i, j, G[i][j]) for j in range(num[0])] for i in range(num[0])]
for i in range(num[1]):
    value = list(map(int, input().split()))
    G[value[0]][value[1]] = G[value[1]][value[0]] = value[2]

for i in range(num[0]):
    for j in range(num[0]):
        for k in range(num[0]):
            G[j][k] = min(G[j][k], G[j][i] + G[i][k])

menor = INF

for i in range(num[0]):
    maior = -1
    for j in range(num[0]):
        if maior < G[i][j]:
            maior = G[i][j]
    if maior < menor:
        menor = maior

print(menor)