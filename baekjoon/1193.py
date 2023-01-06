n = int(input())
line, end = 0, 0
while n > end:
  line += 1
  end += line
order = line - end + n - 1
print(f'{line-order}/{order+1}' if line % 2 else f'{order+1}/{line-order}')
