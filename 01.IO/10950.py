# A+B -3
"""
* Input
5
1 1
2 3
3 4
9 8
5 2

* Output
2
5
7
17
7
"""

n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  print(a+b)
