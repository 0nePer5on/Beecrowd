num = int(input())
for n in range(num):
    entry = input()
    values = entry.split()
    if values[0] == 'Thor' and int(values[1]) > 0:
        print("Y")
    else:
        print("N")