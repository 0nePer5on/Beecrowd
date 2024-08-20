import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        value = input()
        if is_prime(int(value)):
            conf = 0
            for i in value:
                if(is_prime(int(i))):
                    conf += 1;
            if conf == len(value):
                print("Super")
            else:
                print("Primo")
        else:
            print("Nada")
    except EOFError:
        break;
