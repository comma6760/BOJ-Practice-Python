A = input()
stack = []
cnt = 0

for i in range(len(A)):
    if A[i] == '(':
        stack.append("(")
    else:
        if A[i-1] == "(":
            stack.pop()
            cnt += len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운트
            
        else:
            stack.pop()
            cnt += 1 # 두 번째 경우인 나머지 부분을 세는 것
print(cnt)