N,K= map(int, input().split())
scores = map(int, input().split())
print(sorted(scores)[-K])