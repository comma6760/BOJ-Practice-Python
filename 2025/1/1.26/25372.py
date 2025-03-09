N = int(input())

for i in range(N):
    a = input()
    if (len(a) >= 6 and len(a) <= 9):
        print("yes")
    else:
        print("no")