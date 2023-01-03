h, m = map(int, input().split())
timer = int(input())
print((h + (m + timer) // 60) % 24, (m + timer) % 60)
