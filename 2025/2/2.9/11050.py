def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

n,r = map(int, input().split())
print(factorial(n) // (factorial(r) * factorial(n-r)))