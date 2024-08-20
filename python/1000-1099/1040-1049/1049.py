op1 = input()
if op1 == 'vertebrado':
    op2 = input()
    if op2 == 'ave':
        op3 = input()
        if op3 == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        op3 = input()
        if op3 == 'onivoro':
            print("homem")
        else:
            print("vaca")
else:
    op2 = input()
    if op2 == 'inseto':
        op3 = input()
        if op3 == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        op3 = input()
        if op3 == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")