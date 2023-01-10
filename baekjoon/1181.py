words = [input() for i in range(int(input()))]
for word in sorted(list(set(words)), key=lambda x: (len(x), x)):
  print(word)