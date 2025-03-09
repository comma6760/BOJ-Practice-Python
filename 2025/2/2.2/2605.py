student = int(input())
num = list(map(int, input().split()))
result = [0] * 100

for i in range(student):
    result[i] = i + 1
    
    for j in range(i, i-num[i], -1):
        temp = result[j]
        result[j] = result[j-1]
        result[j-1] = temp

for i in range(student):
    print(result[i], end=' ')