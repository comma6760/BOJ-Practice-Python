N, K = map(int, input().split())
coin_list = list()
for i in range(N):
    coin_list.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K // coin_list[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K % coin_list[i] #K는 동전으로 나눈 나머지로 계속 반복
print(count)