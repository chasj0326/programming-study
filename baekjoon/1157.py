word = input().upper()
abc = list(set(word))
counts = [word.count(i) for i in abc]
if counts.count(max(counts))>1:
  print('?')
else:
  print(abc[counts.index(max(counts))])