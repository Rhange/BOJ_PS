import sys

n = int(input())


def fast_input():
  return sys.stdin.readline().rstrip()


count = 0
total = 0
for _ in range(n):
  sol = fast_input()  # input을 더 빠르게 받기
  
  for ox in sol:
    if ox == 'O':
      count += 1
      total += count
    else:
      count = 0

  print(total)
  count, total = 0, 0 # 하나 끝나고 초기화