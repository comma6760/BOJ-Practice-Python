n, p = map(int, input().split())

l = []
r = n

while 1:
    r = (r * n) % p
    if r in l:
        print(len(l) - l.index(r))
        break
    l.append(r)