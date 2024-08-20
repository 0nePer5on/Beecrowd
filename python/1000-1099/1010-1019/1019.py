seconds, minutes, hours = int(input()), 0, 0
if seconds > 60:
    minutes = int(seconds / 60)
    seconds %= 60
if minutes > 60:
    hours = int(minutes / 60)
    minutes %= 60

print(f"{hours}:{minutes}:{seconds}")