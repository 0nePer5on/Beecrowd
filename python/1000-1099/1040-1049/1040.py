n1, n2, n3, n4 = input().split()
media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4)) / 10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media >= 5 and media < 7:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    media = (media + exam) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
else:
    print("Aluno reprovado.")