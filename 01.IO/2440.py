def print_star_antipyramid(n):
  for i in range(n):
    print('*'*(n-i))
  return 0

n = int(input())
print_star_antipyramid(n)