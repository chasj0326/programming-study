from collections import deque

q = deque(input())
num, op = '', ''
answers = []

while q:
  now = q.popleft()
  if now != '-' and now != '+':
    num += now
  if (not q) or now == '-' or now == '+':
    if op == '+':
      answers[-1] += int(num)
    else:
      answers.append(int(num))
    num, op = '', now

for i in range(1, len(answers)):
  answers[i] = answers[i - 1] - answers[i]

print(answers[-1])
