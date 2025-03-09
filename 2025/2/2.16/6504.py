fib = [0] * 21
fib[0] = 1
fib[1] = 2

for i in range(2, 21):
    fib[i] = fib[i-1] + fib[i-2]

for _ in range(int(input())):
    ans = 0
    x = int(input())
    
    for i in range(20,0,-1):
        if x >= fib[i]:
            x -= fib[i]
            ans += fib[i-1]
    
    print(ans)