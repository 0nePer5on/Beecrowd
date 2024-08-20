entry = list(map(int, input().split()))
entry.sort()
conf = False
for i in range(2):
    numbers = entry[i:i+3]
    if numbers[0] + numbers[1] > numbers[2]:
        if numbers[0] + numbers[2] > numbers[1]:
            if numbers[1] + numbers[2] > numbers[0]:
                conf = True
                break
result = "S" if conf else "N"
print(result)