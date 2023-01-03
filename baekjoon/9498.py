x = int(input())
grade = ['F', 'D', 'C', 'B', 'A', 'A']
print(grade[(x - 50) // 10] if x >= 50 else 'F')
