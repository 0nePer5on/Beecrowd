import math

def bhaskara(numbers):
    num = (numbers[1] ** 2) + ((-4) * numbers[0] * numbers[2])
    if math.floor(numbers[0]) == 0 or num < 0:
        print("Impossivel calcular")
        return
    num1 = (numbers[1] * -1 + (num ** 0.5)) / (2 * numbers[0])
    num2 = (numbers[1] * -1 - (num ** 0.5)) / (2 * numbers[0])
    print(f"R1 = {num1:.5f}")
    print(f"R2 = {num2:.5f}")
        
numbers = input().split()
numbers = [eval(i) for i in numbers]
bhaskara(numbers)