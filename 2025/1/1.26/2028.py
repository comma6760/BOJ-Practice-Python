N = int(input())

for i in range(N):
    a = int(input())
    k = len(str(a))
    if str(a**2)[-k:] == str(a):
        print("YES")
    else:
        print("NO")