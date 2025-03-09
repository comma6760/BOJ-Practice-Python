N = int(input())
a = list(map(int, input().split()))

print(min(a))
print(max(a))

# def fibonacci(n):
#     #1에서부터 차근차근 다음 값이 return 
#     cur =0
#     fibo = 1 #현재 수
#     prev_fibo = 0 #이전 수 
#     i =0
#     while i < n:
#         cur = fibo + prev_fibo #다음 피보나치 = 현재 + 이전 
#         prev_fibo = fibo
#         fibo = cur
#         yield fibo
#         i+=1

# a = fibonacci(5)

# for i in a:
#     print(i)