cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
ans = 0
while len(word) > 2:
  ans += 1
  if word[:3] in cro:
    word = word[3:]
  elif word[:2] in cro:
    word = word[2:]
  else:
    word = word[1:]
if word:
  ans += 1 if word in cro or len(word) == 1 else 2
print(ans)
