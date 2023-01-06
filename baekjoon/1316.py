def isGroup(word):
  word, spell, order = list(word), [], []
  for i in word:
    if i not in spell:
      spell.append(i)
      order.append(word.index(i))
    else:
      if (word.index(i) - order[spell.index(i)] != 1):
        return False
      order[spell.index(i)] = word.index(i)
    word[word.index(i)] = 0
  return True


n = int(input())
ans = 0
for i in range(n):
  if isGroup(input()):
    ans += 1

print(ans)
