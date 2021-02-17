def print_star_antipyramid2(n):
  for i in range(n):
    print(f"{' '*i}{'*'*(n-i)}")
  return 0

n = int(input())
print_star_antipyramid2(n)