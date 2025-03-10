up, down, len = map(int, input().split())

day = 1
day += (len - up) / (up - down)
if (len - up) % (up - down) != 0:
    day += 1
if up > len:
    print("1")
else:
    print(day)