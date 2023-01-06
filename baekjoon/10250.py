for i in range(int(input())):
  h, w, n = map(int, input().split())
  floor, number = 0, 0
  number = n // h + 1 if n % h else n // h
  floor = n % h if n % h else h
  print(floor, number, sep='' if number // 10 else '0')