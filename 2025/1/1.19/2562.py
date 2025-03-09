a = [0] * 10
Max = 0
Num = 0

for i in range(9):
    a[i] = int(input())
    
    if a[i] > Max:
        Max = a[i]
        Num = i + 1
print(Max)
print(Num)