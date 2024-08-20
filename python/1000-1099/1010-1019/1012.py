entry = list(input().split())
entry = [eval(i) for i in entry]
pi = 3.14159

print(f"TRIANGULO: {(entry[0] * entry[2]) / 2:.3f}")
print(f"CIRCULO: {pi*entry[2]**2:.3f}")
print(f"TRAPEZIO: {((entry[0] + entry[1]) * entry[2]) / 2:.3f}")
print(f"QUADRADO: {entry[1]**2:.3f}")
print(f"RETANGULO: {entry[0]*entry[1]:.3f}")