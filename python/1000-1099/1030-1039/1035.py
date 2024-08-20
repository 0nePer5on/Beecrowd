def condition(numbers):
    if numbers[1] > numbers[2]:
        if numbers[3] > numbers[0]:
            if numbers[2] + numbers[3] > numbers[0] + numbers[1]:
                if numbers[2] >= 0 and numbers[3] >= 0:
                    if numbers[0] % 2 == 0:
                        print("Valores aceitos")
                        return
    print("Valores nao aceitos")
    
numbers = input().split()
numbers = [eval(i) for i in numbers]

condition(numbers)