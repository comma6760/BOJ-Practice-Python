def check(temp):
    #가로
    for i in range(5):
        if bingo[i] == [0] * 5:
            temp += 1
    #세로
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            temp += 1
    #대각선1
    if all(bingo[i][i] == 0 for i in range(5)):
        temp += 1
    #대각선2
    if all(bingo[i][4-i] == 0 for i in range(5)):
        temp += 1
    return temp

bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []

for _ in range(5):
    speak += list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                cnt += 1
    if cnt >= 12:
        result = check(tmp)
        if result >= 3:
            print(i+1)
            break