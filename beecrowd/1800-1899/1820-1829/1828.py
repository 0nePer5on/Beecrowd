cases = ["Bazinga!", "Raj trapaceou!", "De novo!"]

num = int(input())
for i in range(num):
    result = 0
    entry = list(input().split())
    if entry[0] == entry[1]:
        result = 2
    else:
        if entry[0] == "papel":
            if entry[1] == "tesoura" or entry[1] == "lagarto":
                result = 1
        if entry[0] == "pedra":
            if entry[1] == "papel" or entry[1] == "Spock":
                result = 1
        if entry[0] == "tesoura":
            if entry[1] == "pedra" or entry[1] == "Spock":
                result = 1
        if entry[0] == "lagarto":
            if entry[1] == "pedra" or entry[1] == "tesoura":
                result = 1
        if entry[0] == "Spock":
            if entry[1] == "lagarto" or entry[1] == "papel":
                result = 1
    print(f"Caso #{i + 1}: {cases[result]}")