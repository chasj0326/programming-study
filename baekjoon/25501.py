def recursion(s, l, r, num):
  num += 1
  if l >= r: return (1, num)
  elif s[l] != s[r]: return (0, num)
  else: return recursion(s, l + 1, r - 1, num)

def isPalindrome(s):
  return recursion(s, 0, len(s) - 1, 0)

for _ in range(int(input())):
  print(*isPalindrome(input()))
