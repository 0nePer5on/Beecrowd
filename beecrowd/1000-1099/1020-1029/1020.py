days, months, years = int(input()), 0, 0
if days >= 365:
    years = int(days / 365)
    days %= 365
if days >= 30:
    months = int(days / 30)
    days %= 30
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")