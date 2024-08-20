num1 = list(input().split())
num2 = list(input().split())
total = int(num1[1]) * float(num1[2]) + int(num2[1]) * float(num2[2])
print(f"VALOR A PAGAR: R$ {total:.2f}")