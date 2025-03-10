a = input()+" "
same = 1

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        same += 1
    elif a[i] != a[i+1]:
        break
print(same)