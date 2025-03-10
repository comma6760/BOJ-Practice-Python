a = [[' ' for _ in range(15)] for _ in range(5)]

for i in range(5):
	b = input()
	for j in range(len(b)):
		a[i][j] = b[j]
        
for i in range(15):
    for j in range(5):
        if a[j][i] == ' ': continue
        else:
            print(a[j][i], end='')