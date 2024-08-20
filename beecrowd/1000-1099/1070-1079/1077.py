num = int(input())
operators = "*/+-^"
for n in range(num):
    entry = input()
    if '(' in entry:
        entry = entry.replace('(', '')
        entry = entry.replace(')', '')
    txt = list(entry)
    txt.reverse()
    for i in range(len(txt)):
        if txt[i] in operators:
            aux = txt[i - 1]
            txt[i - 1] = txt[i]
            txt[i] = aux
    entry = ""
    txt.reverse()
    for i in txt:
        entry += i
    print(entry)