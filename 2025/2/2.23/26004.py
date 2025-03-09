N=int(input())
word = input()
H,I,A,R,C = 0,0,0,0,0

for i in word:
    if i == 'H':
        H += 1
        continue
    if i == 'I':
        I += 1
        continue
    if i == 'A':
        A += 1
        continue
    if i == 'R':
        R += 1
        continue
    if i == 'C':
        C += 1
        continue
print(min(H,I,A,R,C))