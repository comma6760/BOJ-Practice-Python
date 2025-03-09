for i in range(3):
    a = list(map(int, input().split()))
    if a.count(0) == 1:
        print("A")
        continue
    if a.count(0) == 2:
        print("B")
        continue
    if a.count(0) == 3:
        print("C")
        continue
    if a.count(0) == 4:
        print("D")
        continue
    else:
        print("E")
        continue