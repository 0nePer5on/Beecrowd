def simpl(num, den):
    if den == 0:
        return num
    return simpl(den, num % den)

num = int(input())
for n in range(num):
    num1, a, den1, op, num2, b, den2 = input().split()
    num1, num2, den1, den2 = int(num1), int(num2), int(den1), int(den2)
    if op == '+':
        totalN = num1 * den2 + num2 * den1
    if op == '-':
        totalN = num1 * den2 - num2 * den1
    if op == '*':
        totalN = num1 * num2
    totalD = den1 * den2
    if op == '/':
        totalN = num1 * den2
        totalD = num2 * den1
    value = simpl(totalN, totalD)
    print(f"{totalN}/{totalD} = {int(totalN / value)}/{int(totalD / value)}")