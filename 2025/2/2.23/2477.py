import sys

K=int(sys.stdin.readline())

#E=1 W=2 S=3 N=4
height = []
width = []
total = []
#동서쪽으로 움직이는 경우와 남북쪽으로 움직이는 경우를 나누어서 리스트에 넣음
for i in range(6):
    dir, lenght = map(int, sys.stdin.readline().split())
    if dir == 1 or dir == 2:
        width.append(lenght)
        total.append(lenght)
    else:
        height.append(lenght)
        total.append(lenght)
        
bigbox = max(height) * max(width)

#세로 최댓값
maxheight = total.index(max(height))
#가로 최댓값
maxwidth = total.index(max(width))

#전체 이동에서 세로 최댓값의 다음 값에서 세로 최댓값 이전의 가로값을 빼준 것이 작은 사각형의 가로값
small1 = abs(total[maxheight-1] - total[(maxheight-5 if maxheight == 5 else maxheight+1)])

small2 = abs(total[maxwidth-1] - total[maxwidth-5 if maxwidth == 5 else maxwidth+1])
area = bigbox - (small1*small2)
print(area*K)