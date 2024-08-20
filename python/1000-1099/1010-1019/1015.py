import math

entry1, entry2 = list(input().split()), list(input().split())
entry1, entry2 = [eval(i) for i in entry1], [eval(i) for i in entry2]
total = math.sqrt((entry2[0] - entry1[0])**2 + (entry2[1] - entry1[1])**2)
print(f"{total:.4f}")