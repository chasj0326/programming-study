n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
scores = list(map(lambda x: x / m * 100, scores))
print(sum(scores) / n)