house = int(input())
rgb_map = [list(map(int, input().split())) for _ in range(house)]
dp = rgb_map[0]

for index in range(1, house):
    temp1 = min(dp[1],dp[2]) + rgb_map[index][0]
    temp2 = min(dp[0],dp[2]) + rgb_map[index][1]
    temp3 = min(dp[0],dp[1]) + rgb_map[index][2]
    
    dp[0] = temp1
    dp[1] = temp2
    dp[2] = temp3
    
print(min(dp))