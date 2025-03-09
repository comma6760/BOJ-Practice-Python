Day = int(input())
check = 0

a = list(map(int, input().split()))

for i in range(5):
	if Day == a[i]:
		check += 1

print(check)