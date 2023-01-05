case_num = int(input())
for i in range(case_num):
  case = list(map(int, input().split()))
  n = case.pop(0)
  case = list(filter(lambda x: x>sum(case)/n, case))
  print(format(len(case)/n*100, '.3f'),'%',sep='')