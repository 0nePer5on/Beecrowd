t1, day1 = input().split()
h1, t1, m1, t2, s1 = input().split()
t1, day2 = input().split()
h2, t1, m2, t2, s2 = input().split()

values = [[int(day1), int(h1), int(m1), int(s1)], [int(day2), int(h2), int(m2), int(s2)]]
total = [0, 0, 0, 0]
mod = 0

total[3] = values[1][3] - values[0][3]
if total[3] < 0:
    total[3] += 60
    mod = -1
total[2] = values[1][2] - values[0][2] + mod
mod = 0
if total[2] < 0:
    total[2] += 60
    mod = -1
total[1] = values[1][1] - values[0][1] + mod
mod = 0
if total[1] < 0:
    total[1] += 24
    mod = -1
total[0] = values[1][0] - values[0][0] + mod

print(f"{total[0]} dia(s)")
print(f"{total[1]} hora(s)")
print(f"{total[2]} minuto(s)")
print(f"{total[3]} segundo(s)")