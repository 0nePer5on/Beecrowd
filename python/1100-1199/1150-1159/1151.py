entry = int(input())
n1, n2 = 0, 1
sequence = []
for i in range(entry):
    sequence.append(str(n1))
    aux = n2
    n2 += n1
    n1 = aux
print(" ".join(sequence))