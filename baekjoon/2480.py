dice = list(map(int, input().split()))
if len(list(set(dice))) == 1:
  print(10000 + dice[0] * 1000)
elif len(list(set(dice))) == 2:
  num = max(dice, key=dice.count)
  print(1000 + num * 100)
else:
  print(max(dice) * 100)
