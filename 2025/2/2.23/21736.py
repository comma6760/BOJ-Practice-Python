import sys
from collections import deque

# input N,M
N, M = map(int, sys.stdin.readline().strip().split())

dr = [-1,0,1,0]
dc = [0,1,0,-1]
ch = [[0] * M for _ in range(N)]

campus = []
Q = deque()

#캠퍼스 정보
for i in range(N):
    #캠퍼스 정보의 첫 번째 행 입력
    campus.append(list(map(str, sys.stdin.readline().strip())))
    
    for j in range(len(campus[i])):
        #만약 도연이가 있다면
        if campus[i][j] == 'I':
            #위치 큐에 도연이 넣기
            Q.append([i,j])
            ch[i][j] = 1
answer = 0

# 큐가 비었을 때까지 반복
while Q:
    #현재 큐의 길이만큼 좌표 꺼내기
    for _ in range(len(Q)):
        #좌표 하나 꺼내기
        r,c = Q.popleft()
        
        #상하좌우 이동
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            
            #캠퍼스 밖을 벗어나지 않고,
            #방문했던 위치도 X
            #벽이 아닌 경우에만 이동
            if 0<=nr<N and 0 <= nc<M and ch[nr][nc] == 0 and campus[nr][nc] != 'X':
                #사람을 만났다면
                if campus[nr][nc] == 'P':
                    #만난 사람의 수 + 1
                    answer += 1
                
                #방문 표시
                ch[nr][nc] = 1
                #해당 좌표에 큐 삽입
                Q.append([nr, nc])

#만난 사람의 수가 1명 이상
if answer:
    #사람 수 출력
    print(answer)
#만난 사람의 수가 0명
else:
    print('TT')