n1 = int(input())
n2 = int(input())
if n2 > n1:
    n1 += n2
    n2 = n1 - n2
    n1 -= n2
sum = 0
for n in range(n2 + 1, n1):
    if(n % 2 == 1):
        sum += n
print(sum)