entry = ()
entry = input().split()
entry = [eval(i) for i in entry]
sortEntry = list(entry)
sortEntry.sort()
for i in sortEntry:
    print(i)
print()
for i in entry:
    print(i)